package org.example._05;

public class Main {
    public static void main(String[] args) {
        String numeroCartao = "4111 1111 1111 1111";
        String validade = "12/2025";

        Cartao cartao = new Visa(numeroCartao, validade); // Troque para a classe correspondente à bandeira do cartão desejado.

        if (cartao.isValido()) {
            System.out.println("Cartão válido");
        } else {
            System.out.println("Cartão inválido");
        }
    }
}
