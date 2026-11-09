# Crie a classe ControleRemoto, onde vamos simular
# o funcionamento de um controle simples:
# (canal, volume e liga/desliga)

from rich import print
from rich.panel import Panel

class ControleRemoto():

    titulo = "Tv"
    ligada = False

    def __init__(self):
        self.canal = 1
        self.maxCanal = 5
        self.volume = 1
        self.maxVolume = 4

    def showPanel(self, titulo, mensagem):
        infoPanel = Panel(f"[white]{mensagem}[/]", title=f"{titulo}", style="white", width=70)
        print(infoPanel)

    def updateVisualInfo(self):
        panelText = ""
        if not self.ligada:
            panelText = f':prohibited: [red] Tv esta desligada [/]'

        else:
            canalText = "CANAL  = "
            for i in range(1, self.maxCanal + 1):
                canalText += (f" {f'[red on white] {i} [/]' if i == self.canal else i}")

            volumeText = "VOLUME = "
            for i in range(1, self.maxVolume + 1):
                volumeText += (f"{f'[black on red] [/]' if i <= self.volume else f'[black on white] [/]'}")

            panelText = f"{canalText}\n{volumeText}"

        self.showPanel(self.titulo, panelText)

    def liga_desliga(self):
        self.ligada = not self.ligada

    def aumentaVolume(self):
        if self.volume < self.maxVolume:
            self.volume += 1
            self.updateVisualInfo()

    def diminuirVolume(self):
        if self.volume > 1:
            self.volume -= 1
            self.updateVisualInfo()

    def mudaCanalMais(self):
        if self.canal < self.maxCanal:
            self.canal += 1
            self.updateVisualInfo()
        elif self.canal == self.maxCanal:
            self.canal = 1
            self.updateVisualInfo()

    def mudaCanalMenos(self):
        if self.canal > 1:
            self.canal -= 1
            self.updateVisualInfo()
        elif self.canal == 1:
            self.canal = self.maxCanal
            self.updateVisualInfo()


control1 = ControleRemoto()
while True:
    control1.updateVisualInfo()
    comando = str(input(f"\n < CH{control1.canal} >  - VOL{control1.volume} + "))
    match comando:
        case '0':
            break
        case '1':
            control1.liga_desliga()
        case '2':
            control1.aumentaVolume()
        case '3':
            control1.diminuirVolume()
        case '4':
            control1.mudaCanalMais()
        case '5':
            control1.mudaCanalMenos()
    print('\n'*10)
