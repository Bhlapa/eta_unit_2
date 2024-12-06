from src.phonebook import Phonebook

class TestPhonebook:

    #Add
    def test_add_nome_invalido_exclamacao(self):
        # Setup
        phonebook = Phonebook()
        resultado_esperado = "Nome invalido"

        # Chamada
        resultado = phonebook.add("!", "999")

        # Avalicação
        assert resultado == resultado_esperado

    def test_add_nome_invalido_at(self):
        # Setup
        phonebook = Phonebook()
        resultado_esperado = "Nome invalido"

        # Chamada
        resultado = phonebook.add("@", "999")

        # Avalicação
        assert resultado == resultado_esperado

    def test_add_nome_invalido_hashtag(self):
        # Setup
        phonebook = Phonebook()
        resultado_esperado = "Nome invalido"

        # Chamada
        resultado = phonebook.add("#", "999")

        # Avalicação
        assert resultado == resultado_esperado

    def test_add_nome_invalido_dolar(self):
         # Setup
        phonebook = Phonebook()
        resultado_esperado = "Nome invalido"

        # Chamada
        resultado = phonebook.add("$", "999")

        # Avalicação
        assert resultado == resultado_esperado

    def test_add_nome_invalido_percentage(self):
        # Setup
        phonebook = Phonebook()
        resultado_esperado = "Nome invalido"

        # Chamada
        resultado = phonebook.add("%", "999")

        # Avalicação
        assert resultado == resultado_esperado

    def test_add_numero_invalido(self):
        # Setup
        phonebook = Phonebook()
        resultado_esperado = "Numero invalido"

        # Chamada
        resultado = phonebook.add("Bhl", "")

        # Avalicação
        assert resultado == resultado_esperado

    def test_add_numero_sucesso(self):
        # Setup
        phonebook = Phonebook()
        resultado_esperado = "Numero adicionado"

        # Chamada
        resultado = phonebook.add("Bhl", "1")

        # Avalicação
        assert resultado == resultado_esperado

    def test_add_nome_ja_cadastrado(self):
        # Setup
        phonebook = Phonebook()
        resultado_esperado = "Nome já cadastrado"

        # Chamada
        phonebook.add("Bhl","0")
        resultado = phonebook.add("Bhl", "1")

        # Avalicação
        assert resultado == resultado_esperado


    #Lookup
    def test_lookup_nome_sucesso(self):
        # Setup
        phonebook = Phonebook()
        resultado_esperado = "2"

        # Chamada
        phonebook.add("Bhl","1")
        phonebook.add("Bhl1", "2")
        phonebook.add("Bhl2", "3")
        resultado = phonebook.lookup("Bhl1")

        # Avalicação
        assert resultado == resultado_esperado

    def test_lookup_nome_falha(self):
        # Setup
        phonebook = Phonebook()
        resultado_esperado = "Usuario não encontrado"

        # Chamada
        phonebook.add("Bhl","0")
        resultado = phonebook.lookup("Bhl1")

        # Avalicação
        assert resultado == resultado_esperado

    #Get_names
    def test_get_name(self):
        # Setup
        phonebook = Phonebook()
        resultado_esperado = ['POLICIA']

        # Chamada
        resultado = phonebook.get_names()

        # Avalicação
        assert resultado == resultado_esperado

    #Get_number
    def test_get_number(self):
        # Setup
        phonebook = Phonebook()
        resultado_esperado = ['190']

        # Chamada
        resultado = phonebook.get_numbers()

        # Avalicação
        assert resultado == resultado_esperado

    #Clear
    def test_clear_sucesso(self):
        # Setup
        phonebook = Phonebook()
        resultado_esperado = 'phonebook limpado'

        # Chamada
        resultado = phonebook.clear()

        # Avalicação
        assert resultado == resultado_esperado

    #Search
    def test_search_sucesso(self):
        # Setup
        phonebook = Phonebook()
        resultado_esperado = [{'Breno','3'}]

        # Chamada
        phonebook.add("Dreno", "1")
        phonebook.add("Creno", "2")
        phonebook.add("Breno", "3")
        resultado = phonebook.search("Breno")

        # Avalicação
        assert resultado == resultado_esperado

    def test_search_falha(self):
        # Setup
        phonebook = Phonebook()
        resultado_esperado = "Usuario não encontrado"

        # Chamada
        phonebook.add("Dreno", "1")
        phonebook.add("Creno", "2")
        phonebook.add("Breno", "3")
        resultado = phonebook.search("ter")

        # Avalicação
        assert resultado == resultado_esperado

    #Sort
    def test_sort(self):
        # Setup
        phonebook = Phonebook()
        resultado_esperado = ['Breno', 'Creno', 'Dreno', 'POLICIA']

        # Chamada
        phonebook.add("Dreno", "1")
        phonebook.add("Creno", "2")
        phonebook.add("Breno", "3")
        resultado = phonebook.get_phonebook_sorted()

        # Avalicação
        assert resultado == resultado_esperado


    #Sort Reverse
    def test_sort_reverse(self):
        # Setup
        phonebook = Phonebook()
        resultado_esperado = ['POLICIA', 'Dreno', 'Creno', 'Breno']

        # Chamada
        phonebook.add("Dreno", "1")
        phonebook.add("Creno", "2")
        phonebook.add("Breno", "3")
        resultado = phonebook.get_phonebook_reverse()

        # Avalicação
        assert resultado == resultado_esperado


    #Delete
    def test_delete_sucesso(self):
        # Setup
        phonebook = Phonebook()
        resultado_esperado = "Numero deletado"

        # Chamada
        phonebook.add("Dreno", "1")
        phonebook.add("Creno", "2")
        phonebook.add("Breno", "3")
        resultado = phonebook.delete("Creno")

        # Avalicação
        assert resultado == resultado_esperado

    def test_delete_falha(self):
        # Setup
        phonebook = Phonebook()
        resultado_esperado = "Usuario não encontrado"

        # Chamada
        phonebook.add("Dreno", "1")
        phonebook.add("Creno", "2")
        phonebook.add("Breno", "3")
        resultado = phonebook.delete("hue")

        # Avalicação
        assert resultado == resultado_esperado

    #Change Number
    def test_change_number_sucesso(self):
        # Setup
        phonebook = Phonebook()
        resultado_esperado = "Numero alterado"

        # Chamada
        phonebook.add("Dreno", "1")
        phonebook.add("Creno", "2")
        phonebook.add("Breno", "3")
        resultado = phonebook.change_number("Creno","99")

        # Avalicação
        assert resultado == resultado_esperado

    def test_change_number_falha(self):
        # Setup
        phonebook = Phonebook()
        resultado_esperado = "Usuario não encontrado"

        # Chamada
        phonebook.add("Dreno", "1")
        phonebook.add("Creno", "2")
        phonebook.add("Breno", "3")
        resultado = phonebook.change_number("hue","99")

        # Avalicação
        assert resultado == resultado_esperado

#Get name by number
    def test_get_name_by_number_sucesso(self):
        # Setup
        phonebook = Phonebook()
        resultado_esperado = "Creno"

        # Chamada
        phonebook.add("Dreno", "1")
        phonebook.add("Creno", "2")
        phonebook.add("Breno", "3")
        resultado = phonebook.get_name_by_number("2")

        # Avalicação
        assert resultado == resultado_esperado

    def test_get_name_by_number_falha(self):
        # Setup
        phonebook = Phonebook()
        resultado_esperado = "Valor não encontrado."

        # Chamada
        phonebook.add("Dreno", "1")
        phonebook.add("Creno", "2")
        phonebook.add("Breno", "3")
        resultado = phonebook.get_name_by_number("4")

        # Avalicação
        assert resultado == resultado_esperado