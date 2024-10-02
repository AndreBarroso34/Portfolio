import java.util.Scanner;

public class JogoGalo {
    private int jogo[][] = new int[3][3];

    public JogoGalo() {
        // Inicializa o jogo com 0 para representar espaços vazios
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                jogo[i][j] = 0; // Alterado de ' ' para 0
            }
        }
    }

    public void mostrar() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                // Exibe o valor apropriado: 1 para X, 2 para O, 0 para vazio
                System.out.print((jogo[i][j] == 0 ? '-' : (jogo[i][j] == 1 ? 'X' : 'O')) + " ");
            }
            System.out.println();
        }
    }

    public int verificarVencedor() {
        // Verifica linhas
        for (int i = 0; i < 3; i++) {
            if ((jogo[i][0] == jogo[i][1]) && (jogo[i][0] == jogo[i][2]) && (jogo[i][0] != 0)) {
                return jogo[i][0];
            }
        }
        // Verifica colunas
        for (int j = 0; j < 3; j++) {
            if ((jogo[0][j] == jogo[1][j]) && (jogo[0][j] == jogo[2][j]) && (jogo[0][j] != 0)) {
                return jogo[0][j];
            }
        }
        // Verifica diagonais
        if ((jogo[0][0] == jogo[1][1]) && (jogo[0][0] == jogo[2][2]) && (jogo[0][0] != 0)) {
            return jogo[0][0];
        }
        if ((jogo[0][2] == jogo[1][1]) && (jogo[0][2] == jogo[2][0]) && (jogo[0][2] != 0)) {
            return jogo[0][2];
        }
        // Verifica se ainda há espaços vazios
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (jogo[i][j] == 0) {
                    return 0; // Jogo em andamento
                }
            }
        }
        return 3; // Empate
    }

    public boolean efetuarJogada(int jogador, int linha, int coluna) {
        // Verifica se a linha e a coluna estão dentro dos limites
        if (linha < 0 || linha > 2 || coluna < 0 || coluna > 2) {
            return false; // Jogada inválida
        }
        // Verifica se a posição já está ocupada
        if (jogo[linha][coluna] != 0) {
            return false; // Jogada inválida
        }
        // Realiza a jogada
        jogo[linha][coluna] = jogador;
        return true; // Jogada válida
    }

    public static void main(String[] argumentos) {
        Scanner teclado = new Scanner(System.in);
        JogoGalo jogo = new JogoGalo();
        int jogador = 1;
        int vencedor;

        jogo.mostrar();
        while ((vencedor = jogo.verificarVencedor()) == 0) {
            System.out.println("Jogador " + jogador);
            System.out.print("Linha: ");
            int linha = teclado.nextInt();
            System.out.print("Coluna: ");
            int coluna = teclado.nextInt();
            if (!jogo.efetuarJogada(jogador, linha - 1, coluna - 1)) {
                System.out.println("Jogada inválida...");
            } else {
                jogador = (jogador == 1) ? 2 : 1; // Alterna entre os jogadores
            }
            jogo.mostrar();
        }
        switch (vencedor) {
            case 1:
                System.out.println("Vencedor jogador 1");
                break;
            case 2:
                System.out.println("Vencedor jogador 2");
                break;
            case 3:
                System.out.println("Empate");
                break;
        }
        teclado.close(); // Fecha o scanner
    }
}
