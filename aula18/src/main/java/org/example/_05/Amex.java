package org.example._05;

class Amex extends Cartao {
    public Amex(String numero, String validade) {
        super(numero, validade);
    }

    @Override
    public boolean isValido() {
        try {
            isValidDataValidade(validade);
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
            return false;
        }

        return numero.matches("^3[47]\\d{13}$");
    }
}
