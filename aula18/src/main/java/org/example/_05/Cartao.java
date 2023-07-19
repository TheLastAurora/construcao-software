package org.example._05;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;

public abstract class Cartao {
    protected String numero;
    protected String validade;

    public Cartao(String numero, String validade) {
        this.numero = formatarNumero(numero);
        this.validade = validade;
    }

    public abstract boolean isValido();

    protected boolean isValidDataValidade(String validade) {
        Date dataValidade;
        try {
            dataValidade = new SimpleDateFormat("MM/yyyy").parse(validade);
        } catch (ParseException e) {
            throw new IllegalArgumentException("Data de validade inválida");
        }

        Calendar calValidade = new GregorianCalendar();
        calValidade.setTime(dataValidade);

        Calendar calTemp = new GregorianCalendar();
        Calendar calHoje = (GregorianCalendar) calValidade.clone();
        calHoje.set(Calendar.MONTH, calTemp.get(Calendar.MONTH));
        calHoje.set(Calendar.YEAR, calTemp.get(Calendar.YEAR));

        if (calHoje.before(calValidade)) {
            return true;
        } else {
            throw new IllegalArgumentException("Data de validade expirada");
        }
    }

    protected String formatarNumero(String numero) {
        StringBuilder formatado = new StringBuilder();
        for (int i = 0; i < numero.length(); i++) {
            char c = numero.charAt(i);
            if (Character.isDigit(c)) {
                formatado.append(c);
            }
        }
        return formatado.toString();
    }
}

