using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace jogo
{
    public partial class Form1 : Form
    {
        //variaveis 
        bool goLeft, goRight, jumping, isGameOver;

        
        int jumpSpeed;
        int force;
        int score = 0;
        int playerSpeed = 7;

        //velocidade da placa vertical e horizontal
        int horizontalSpeed = 5;
        int verticalSpeed = 3;

        //velocidade dos inimigos
        int enemyOneSpeed = 5;
        int enemyTwoSpeed = 3;


        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void enemyTwo_Click(object sender, EventArgs e)
        {

        }

        private void enemyOne_Click(object sender, EventArgs e)
        {

        }

        private void pictureBox32_Click(object sender, EventArgs e)
        {

        }

        private void pictureBox26_Click(object sender, EventArgs e)
        {

        }

        private void pictureBox27_Click(object sender, EventArgs e)
        {

        }

        private void pictureBox28_Click(object sender, EventArgs e)
        {

        }

        private void pictureBox29_Click(object sender, EventArgs e)
        {

        }

        private void pictureBox30_Click(object sender, EventArgs e)
        {

        }

        private void pictureBox31_Click(object sender, EventArgs e)
        {

        }

        private void MainGameTimerEvent(object sender, EventArgs e)
        {
            //O score do jogador durante o jogo
            txtScore.Text = "Score: " + score;

            //independentemente da velocidade ele empurra o jogador para cima ou para baixo da plataforma
            player.Top += jumpSpeed;


            if (goLeft == true)
            {
                player.Left -= playerSpeed;
            }
            if (goRight == true)
            {
                player.Left += playerSpeed;
            }

            //se a força do salto for 0 ele nao salta
            if (jumping == true && force < 0)
            {
                jumping = false;
            }

            //se ele saltar a força passa para 1
            if (jumping == true)
            {
                jumpSpeed = -8;
                force -= 1;
            }
            else
            {
                jumpSpeed = 10;
            }

            //loop para as plataformas se mexerem
            foreach (Control x in this.Controls)
            {
                if (x is PictureBox)
                {
                    if ((string)x.Tag == "platform")
                    {
                        if (player.Bounds.IntersectsWith(x.Bounds))
                        {
                            force = 8;
                            player.Top = x.Top - player.Height;
                            if ((string)x.Name == "horizontalPlatform" && goLeft == false || (string)x.Name == "horizontalPlatform" && goRight == false)
                            {
                                player.Left -= horizontalSpeed;
                            }
                        }
                        x.BringToFront();
                    }
                    if ((string)x.Tag == "coin")
                    {
                        if (player.Bounds.IntersectsWith(x.Bounds) && x.Visible == true)
                        {
                            x.Visible = false;
                            score++;
                        }
                    }
                    if ((string)x.Tag == "enemy")
                    {
                        if (player.Bounds.IntersectsWith(x.Bounds))
                        {
                            GamerTimer.Stop();
                            isGameOver = true;
                            txtScore.Text = "Score: " + score + Environment.NewLine + "You were killed in your journey!!";
                        }
                    }
                }
            }

            //plataformas só se movimentam na horizontal
            horizontalPlatform.Left -= horizontalSpeed;

            if (horizontalPlatform.Left < 0 || horizontalPlatform.Left + horizontalPlatform.Width > this.ClientSize.Width)
            {
                horizontalSpeed = -horizontalSpeed;
            }

            //platafromas só se movimentam na vertical
            verticalPlatform.Top += verticalSpeed;


            if (verticalPlatform.Top < 195 || verticalPlatform.Top > 581)
            {
                verticalSpeed = -verticalSpeed;
            }

            //inimigos movimenta-se na vertical
            enemyOne.Left -= enemyOneSpeed;
            if (enemyOne.Left < pictureBox5.Left || enemyOne.Left + enemyOne.Width > pictureBox5.Left + pictureBox5.Width)
            {
                enemyOneSpeed = -enemyOneSpeed;
            }
            enemyTwo.Left += enemyTwoSpeed;
            if (enemyTwo.Left < pictureBox2.Left || enemyTwo.Left + enemyTwo.Width > pictureBox2.Left + pictureBox2.Width)
            {
                enemyTwoSpeed = -enemyTwoSpeed;
            }
            if (player.Top + player.Height > this.ClientSize.Height + 50)
            {
                GamerTimer.Stop();  
                isGameOver = true;
                txtScore.Text = "Score: " + score + Environment.NewLine + "You fell to your death!";
            }

            //se nao tens todas as coins mostrar a frase para colectar as coins, mas se ja tiver todas diz que 
            if (player.Bounds.IntersectsWith(door.Bounds) && score == 26)
            {
                GamerTimer.Stop();
                isGameOver = true;
                txtScore.Text = "Score: " + score + Environment.NewLine + "Your quest is complete!";
            }
            else
            {
                txtScore.Text = "Score: " + score + Environment.NewLine + "Collect all the coins";
            }



        }

        private void Keylisdown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Left)
            {
                goLeft = true;
            }
            if (e.KeyCode == Keys.Right)
            {
                goRight = true;
            }

            //se clicar no espaço , salta
            if (e.KeyCode == Keys.Space && jumping == false)
            {
                jumping = true;
            }

        }

        private void KeyIsUp(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Left)
            {
                goLeft = false;
            }

            if (e.KeyCode == Keys.Right)
            {
                goRight = false;
            }

            if (jumping == true)
            {
                jumping = false;
            }

            //se precionarmos a tecla enter o jogo recomeça
            if (e.KeyCode == Keys.Enter && isGameOver == true)
            {
                RestartGame();
            }


        }

        //funcao para resetar o jogo
        private void RestartGame()
        {

            //Variaveis
            jumping = false;
            goLeft = false;
            goRight = false;
            isGameOver = false;
            score = 0;

            //quando resetar o jogo, o score volta a 0
            txtScore.Text = "Score: " + score;

            //Por as caixas de imagem visiveis(plataformas,coins,inimigos e player)
            foreach (Control x in this.Controls)
            {
                if (x is PictureBox && x.Visible == false)
                {
                    x.Visible = true;
                }
            }

            //resetar os players, inimigos  e plataformas horizontais e verticais
            player.Left = 72;
            player.Top = 656;


            enemyOne.Left = 471;
            enemyTwo.Left = 360;

            horizontalPlatform.Left = 275;
            verticalPlatform.Top = 581;

            //O tempo começar
            GamerTimer.Start(); 


        }
    }
}
