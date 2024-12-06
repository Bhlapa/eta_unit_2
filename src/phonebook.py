from collections import OrderedDict


class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    def add(self, name, number):
        """
        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado' or 'Nome já cadastrado'
        """

        #Melhoria - Centralizar validação em 1 unico if
        if any(char in name for char in ['!', '@', '#', '$', '%']):
            return 'Nome invalido'

        #BUG - Mensagem de retorno sem o "o" de "invalido"
        #Melhoria - Código modificado para não permitir o cadastro com número vazio
        if len(number) <=0:
            return 'Numero invalido'

        if name not in self.entries:
            self.entries[name] = number
            return 'Numero adicionado'

        #Melhoria - Avisa ao usuário que o nome já existe e por isso não será cadastrado
        else:
            return 'Nome já cadastrado'

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name or 'Usuario não encontrado'
        """

        # Melhoria - Código foi modificado para só retornar número de usuários que existam e se o usuário não existir uma mensagem será exibida para o usuário
        if name in self.entries:
            return self.entries[name]
        else:
            return "Usuario não encontrado"

    def get_names(self):
        """
        :return: return all names in phonebook
        """
        # Melhoria - Cast de list para transformar o resultado
        return list(self.entries.keys())

    def get_numbers(self):
        """
        :return: return all numbers in phonebook
        """
        # Melhoria - Cast de list para transformar o resultado
        return list(self.entries.values())

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        #Melhoria - Retornando o dicionario para o estado padrão
        self.entries = {'POLICIA': '190'}
        return 'phonebook limpado'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search or 'Usuario não encontrado'
        """
        result = []
        for name, number in self.entries.items():
            #BUG - Função está retornando todos os usuário menos o que foi solicitado
            if search_name in name:
                result.append({name, number})
                return result
        #Melhoria - retorno caso o usuário não exista na lista
        return "Usuario não encontrado"



    def get_phonebook_sorted(self):
        """
        :return: return phonebook in sorted order
        """
        #BUG - Função não realizava nenhum sort, apenas retornava o dicionario
        self.entries = OrderedDict(sorted(self.entries.items()))
        #Melhoria - Cast de list para transformar o resultado
        return list(self.entries)

    def get_phonebook_reverse(self):
        """
        :return: return phonebook in reverse sorted order
        """
        #BUG - Função não realizava nenhum sort, apenas retornava a lista
        self.entries = OrderedDict(sorted(self.entries.items(), reverse=True))
        # Melhoria - Cast de list para transformar o resultado
        return list(self.entries)

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        #Melhoria - validação para saber se o usuário existe
        if name in self.entries:
            self.entries.pop(name)
            return 'Numero deletado'
        else:
            return "Usuario não encontrado"

    def change_number(self, name, number):
        if name in self.entries:
            self.entries[name] = number
            return "Numero alterado"
        else:
            return "Usuario não encontrado"

    def get_name_by_number(self, number):
        for name, val in self.entries.items():
            if val == number:
                return name
        return "Valor não encontrado."


