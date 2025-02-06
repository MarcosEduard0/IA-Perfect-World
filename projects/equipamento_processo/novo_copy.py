import frida
import sys


def on_message(message, data):
    print("[Mensagem do Script]", message)


try:
    # Anexa ao processo "elementclient_64.exe"
    session = frida.attach("elementclient_64.exe")
except Exception as e:
    print("Erro ao anexar no processo:", e)
    sys.exit(1)

# Script JavaScript que será injetado
script_code = """
// Obtém o endereço base do módulo
var moduleBase = Module.findBaseAddress("elementclient_64.exe");
if (moduleBase === null) {
    send("Não foi possível encontrar o endereço base do módulo.");
} else {
    // Calcula o endereço da instrução alvo: elementclient_64.exe + 0x8BACC3
    var targetAddress = moduleBase.add(0x8BACC3);
    send("Instrução alvo: " + targetAddress);
    
    // Armazena o objeto do hook numa variável para que possamos removê-lo posteriormente
    var hook = Interceptor.attach(targetAddress, {
        onEnter: function(args) {
            // Calcula o endereço do HP a partir do valor de RDI + 0x92C
            var hpAddress = this.context.rdi.add(0x92C);
            // Lê um inteiro (32 bits) a partir desse endereço
            var hpValue = Memory.readInt(hpAddress);
            send("RDI: " + this.context.rdi + " | HP Address: " + hpAddress + " | HP Value: " + hpValue);
            // Remove o hook para que não entre em loop
            hook.detach();
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
