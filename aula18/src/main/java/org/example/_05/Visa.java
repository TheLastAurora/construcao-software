package org.example._05;


class Visa extends Cartao {
    public Visa(String numero, String validade) {
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

        return numero.matches("^4(\\d{12}|\\d{15})$");
    }
}