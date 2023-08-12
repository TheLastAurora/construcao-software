package org.example._05;

class MasterCard extends Cartao {
    public MasterCard(String numero, String validade) {
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

        return numero.matches("^5[1-5]\\d{14}$");
    }
}
