#include <windows.h>
#include <tlhelp32.h>
#include <iostream>
#include <string>
#include <algorithm>

// Função para obter o PID de um processo pelo nome do executável
DWORD GetProcessIdByName(const char *processName)
{
    DWORD pid = 0;
    HANDLE hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
    if (hSnapshot == INVALID_HANDLE_VALUE)
    {
        std::cerr << "Erro ao criar snapshot de processos." << std::endl;
        return 0;
    }

    PROCESSENTRY32 pe32;
    pe32.dwSize = sizeof(PROCESSENTRY32);

    // Enumera processos
    if (Process32First(hSnapshot, &pe32))
    {
        do
        {
            // _stricmp faz comparação case-insensitive
            if (_stricmp(pe32.szExeFile, processName) == 0)
            {
                pid = pe32.th32ProcessID;
                break;
            }
        } while (Process32Next(hSnapshot, &pe32));
    }

    CloseHandle(hSnapshot);
    return pid;
}

// Função para imprimir todos os módulos de um processo (para debug)
void PrintAllModules(DWORD pid)
{
    HANDLE hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPMODULE, pid);
    if (hSnapshot == INVALID_HANDLE_VALUE)
    {
        std::cerr << "Erro ao criar snapshot de módulos." << std::endl;
        return;
    }

    MODULEENTRY32 me32;
    me32.dwSize = sizeof(MODULEENTRY32);

    std::cout << "[Módulos do Processo PID=" << pid << "]" << std::endl;

    if (Module32First(hSnapshot, &me32))
    {
        do
        {
            std::cout << " - Nome do módulo: " << me32.szModule
                      << " | Endereço Base: 0x" << std::hex << (uintptr_t)me32.modBaseAddr
                      << std::dec << std::endl;
        } while (Module32Next(hSnapshot, &me32));
    }
    CloseHandle(hSnapshot);
}

// Função para obter o endereço base de um módulo específico no processo
uintptr_t GetModuleBaseAddress(DWORD processId, const char *moduleName)
{
    uintptr_t baseAddress = 0;

    HANDLE hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPMODULE, processId);
    if (hSnapshot == INVALID_HANDLE_VALUE)
    {
        std::cerr << "Erro ao criar snapshot de módulos." << std::endl;
        return 0;
    }

    MODULEENTRY32 me32;
    me32.dwSize = sizeof(MODULEENTRY32);

    if (Module32First(hSnapshot, &me32))
    {
        do
        {
            // Verifica o nome do módulo (case-insensitive)
            if (_stricmp(me32.szModule, moduleName) == 0)
            {
                baseAddress = (uintptr_t)me32.modBaseAddr;
                break;
            }
        } while (Module32Next(hSnapshot, &me32));
    }

    CloseHandle(hSnapshot);
    return baseAddress;
}

int main()
{
    // Substitua por seu executável alvo
    const char *processName = "elementclient_64.exe";

    // 1. Obter o PID do processo
    DWORD pid = GetProcessIdByName(processName);
    if (pid == 0)
    {
        std::cout << "Não foi possível encontrar o processo: " << processName << std::endl;
        return 1;
    }
    std::cout << "PID do processo " << processName << ": " << pid << std::endl;

    // 2. (Opcional) Imprimir todos os módulos do processo para debug
    PrintAllModules(pid);

    // 3. Obter o endereço base do módulo (caso seja necessário)
    uintptr_t baseAddress = GetModuleBaseAddress(pid, processName);
    if (baseAddress == 0)
    {
        std::cout << "Erro ao obter o endereço base do módulo " << processName << std::endl;
        return 1;
    }

    // 4. Imprime o endereço em formato hexadecimal
    std::cout << "Endereço base de " << processName << ": 0x"
              << std::hex << baseAddress << std::dec << std::endl;

    return 0;
}
