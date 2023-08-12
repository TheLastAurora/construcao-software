package org.example._05;

class Diners extends Cartao {
    public Diners(String numero, String validade) {
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

        return numero.matches("^3[68]\\d{12}|0[0-5]\\d{11}$");
    }
}