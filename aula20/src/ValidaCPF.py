class ValidaCPF:
    def is_cpf(self, cpf):
        result = False
        numeros_cpf = [0] * 11
        quantidade_zeros = 11 - len(cpf)
        soma = 0

        if len(cpf) > 11:
            return result

        if len(cpf) < 3:
            return result

        if not cpf.isdigit():
            return result

        for i in range(quantidade_zeros):
            numeros_cpf[i] = 0

        j = 0
        for i in range(quantidade_zeros, 11):
            numeros_cpf[i] = int(cpf[j])
            j += 1

        if all(x == numeros_cpf[0] for x in numeros_cpf[1:]):
            return result

        for i in range(len(numeros_cpf) - 2):
            soma += numeros_cpf[i] * (10 - i)

        resto_divisao_primeiro_digito = soma % 11
        primeiro_digito = 0 if resto_divisao_primeiro_digito < 2 else 11 - \
            resto_divisao_primeiro_digito

        soma = 0
        for i in range(len(numeros_cpf) - 1):
            soma += numeros_cpf[i] * (11 - i)

        resto_divisao_segundo_digito = soma % 11
        segundo_digito = 0 if resto_divisao_segundo_digito < 2 else 11 - \
            resto_divisao_segundo_digito

        result = primeiro_digito == numeros_cpf[9] and segundo_digito == numeros_cpf[10]

        return result


validator = ValidaCPF()