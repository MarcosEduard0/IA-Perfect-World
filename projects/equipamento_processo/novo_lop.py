import frida
import sys


def on_message(message, data):
    # Callback para as mensagens enviadas pelo script injetado
    print("[Mensagem do Script] ", message)
    # Se desejar encerrar logo após receber a mensagem, pode:
    # sys.exit(0)


try:
    # Anexa ao processo "elementclient_64.exe"
    session = frida.attach("elementclient_64.exe")
except Exception as e:
    print("Erro ao anexar no processo:", e)
    sys.exit(1)

# Script JavaScript que será injetado
script_code = """
// Obter o endereço base do módulo
var moduleBase = Module.findBaseAddress("elementclient_64.exe");
if (moduleBase === null) {
    send("Não foi possível encontrar o endereço base do módulo.");
} else {
    // Calcula o endereço da instrução onde queremos interceptar
    // Neste exemplo, usamos o offset 0x8BACC3 (isto é: elementclient_64.exe+8BACC3)
    var targetAddress = moduleBase.add(0x8BACC3);
    send("Instrução alvo: " + targetAddress);
    
    // Intercepta a execução nessa instrução
    Interceptor.attach(targetAddress, {
        onEnter: function(args) {
            // Calcula o endereço do HP a partir do valor de RDI + 0x92C
            var hpAddress = this.context.rdi.add(0x92C);
            // Lê um inteiro (32 bits) a partir desse endereço
            var hpValue = Memory.readInt(hpAddress);
            send("RDI: " + this.context.rdi + " | HP Address: " + hpAddress + " | HP Value: " + hpValue);
            // Após interceptar uma vez, desativa o hook para não ficar chamando repetidamente.
            this.detach();
        }
    });
}
"""

# Cria e carrega o script
script = session.create_script(script_code)
script.on("message", on_message)
script.load()

print("Script injetado. Aguardando a execução da instrução interceptada...")
sys.stdin.read()
