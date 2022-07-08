using System;
using System.Windows.Forms;

namespace HelloWorldCSharp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            System.Console.WriteLine("Hello World!");
        }

        private void button1_Click(object sender, EventArgs e)
        {
            button1.Text = "Hello World!";
        }
    }
}
