using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Windows.Forms;
using Tesseract;
using System.Threading.Tasks;

namespace PerfectWorldOCR
{
    public partial class MainForm : Form
    {
        private Bitmap gameScreenshot;
        private readonly string tesseractPath = @"C:\\Program Files\\Tesseract-OCR";
        private Dictionary<string, int> atributos = new Dictionary<string, int>();

        public MainForm()
        {
            InitializeComponent();
            InicializarDropdowns();
        }

        private void InicializarDropdowns()
        {
            List<string> atributosDisponiveis = new List<string>
            {
                "Ataque Magico", "Penetracao Magica", "Ataque Fisico",
                "Penetracao Fisica", "Espirito", "Defesa", "Defesa Magica", "HP"
            };

            comboBoxAtributos.DataSource = new BindingSource(atributosDisponiveis, null);
        }

        private void btnCapturarTela_Click(object sender, EventArgs e)
        {
            gameScreenshot = CapturarTela();
            pictureBoxScreenshot.Image = gameScreenshot;
        }

        private Bitmap CapturarTela()
        {
            Rectangle bounds = Screen.PrimaryScreen.Bounds;
            Bitmap screenshot = new Bitmap(bounds.Width, bounds.Height);
            using (Graphics g = Graphics.FromImage(screenshot))
            {
                g.CopyFromScreen(Point.Empty, Point.Empty, bounds.Size);
            }
            return screenshot;
        }

        private void btnExecutarOCR_Click(object sender, EventArgs e)
        {
            if (gameScreenshot == null)
            {
                MessageBox.Show("Por favor, capture uma tela primeiro.", "Aviso", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }
            
            atributos = ProcessarOCR(gameScreenshot);
            ExibirResultados();
        }

        private Dictionary<string, int> ProcessarOCR(Bitmap imagem)
        {
            Dictionary<string, int> resultado = new Dictionary<string, int>();
            using (var engine = new TesseractEngine(tesseractPath, "por", EngineMode.Default))
            {
                using (var page = engine.Process(imagem))
                {
                    string textoOCR = page.GetText();
                    resultado = ContarAtributos(textoOCR);
                }
            }
            return resultado;
        }

        private Dictionary<string, int> ContarAtributos(string texto)
        {
            Dictionary<string, int> contagem = new Dictionary<string, int>()
            {
                {"Ataque Magico", texto.Split(new string[] {"AtaM", "AtqM"}, StringSplitOptions.None).Length - 1},
                {"Penetracao Magica", texto.Split(new string[] {"Mágica", "Magica"}, StringSplitOptions.None).Length - 1},
                {"Ataque Fisico", texto.Split(new string[] {"físico", "fisico"}, StringSplitOptions.None).Length - 1},
                {"Penetracao Fisica", texto.Split(new string[] {"Física", "Fisica"}, StringSplitOptions.None).Length - 1},
                {"Espirito", texto.Split(new string[] {"Espírito", "Espirito"}, StringSplitOptions.None).Length - 1},
                {"Defesa", texto.Split(new string[] {"Def"}, StringSplitOptions.None).Length - 1},
                {"Defesa Magica", texto.Split(new string[] {"DefM"}, StringSplitOptions.None).Length - 1},
                {"HP", texto.Split(new string[] {"HP"}, StringSplitOptions.None).Length - 1}
            };
            return contagem;
        }

        private void ExibirResultados()
        {
            string atributoSelecionado = comboBoxAtributos.SelectedItem.ToString();
            if (atributos.ContainsKey(atributoSelecionado))
            {
                lblResultado.Text = $"{atributoSelecionado}: {atributos[atributoSelecionado]}";
            }
            else
            {
                lblResultado.Text = "Nenhum valor encontrado";
            }
        }
    }
}
