import frida
import sys


def on_message(message, data):
    print("[Mensagem do Script]", message)


try:
    session = frida.attach("elementclient_64.exe")
except Exception as e:
    print("Erro ao anexar no processo:", e)
    sys.exit(1)

script_code = r"""
var moduleBase = Module.findBaseAddress("elementclient_64.exe");
if (moduleBase === null) {
    send("Não foi possível encontrar o endereço base do módulo.");
} else {
    var targetAddress = moduleBase.add(0x91BA50);
    send("Hookando em: " + targetAddress);

    Interceptor.attach(targetAddress, {
        onEnter: function(args) {
            var rdxVal = this.context.rdx;
            if (rdxVal === undefined) {
                send("rdxVal está undefined.");
                return;
            }
            var edxLower32 = rdxVal.toNumber() & 0xFFFFFFFF;

            var r9Val = this.context.r9;
            send("[ENTER] RDX(64) = 0x" + rdxVal.toString(16) +
                 " | EDX(32) = 0x" + edxLower32.toString(16) +
                 " | R9 = 0x" + r9Val.toString(16));

            if (!r9Val.isNull()) {
                try {
                    var rawData = Memory.readByteArray(r9Val, 0x1C);

                    // Converte manualmente para string hexa:
                    var byteArray = new Uint8Array(rawData);
                    var hexStr = "";
                    for (var i = 0; i < byteArray.length; i++) {
                        hexStr += ("0" + byteArray[i].toString(16).toUpperCase()).slice(-2) + " ";
                    }
                    send("Conteúdo [r9] (0x1C bytes):\n" + hexStr);

                } catch (ex) {
                    send("Falha ao ler [r9]: " + ex);
                }
            }
        }
    });
}
"""

script = session.create_script(script_code)
script.on("message", on_message)
script.load()

print("Script injetado. Aguardando a execução da instrução interceptada...")
sys.stdin.read()
