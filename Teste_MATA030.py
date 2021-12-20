from tir import Webapp
import unittest

class MATA030(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.grupo = "99"

        inst.oHelper = Webapp() 
        inst.oHelper.Setup('SIGAFAT','20/12/2021', inst.grupo, '01', '05')
        inst.oHelper.Program('MATA030')

    def teste_MATA030_001(self):

        csv_content_dictionary = self.oHelper.OpenCSV(delimiter=";", csv_file="SA1_1.csv", header=True)

        # Alguns casos abaixo o meu .CSV precisou de ajustes no conteudo retornado, 
        # isso é mais um exemplo do poder de programação que pode ser utilizado aqui no script

        a1_cod2	    = csv_content_dictionary['A1_COD']    
        a1_cod2     = {k: str(v) for k, v in a1_cod2.items()} # Converto tudo para string    
        a1_loja	    = csv_content_dictionary['A1_LOJA']        
        a1_loja 	= {k: '0'+str(v) for k, v in a1_loja.items()} # Converto tudo para string e insiro o prefixo 0.
        a1_pessoa	= csv_content_dictionary['A1_PESSOA']
        a1_nome		= csv_content_dictionary['A1_NOME']
        a1_nreduz	= csv_content_dictionary['A1_NREDUZ']
        a1_end		= csv_content_dictionary['A1_END']
        a1_tipo		= csv_content_dictionary['A1_TIPO']
        a1_tipo 	= {k: 'F' for k, v in a1_tipo.items()}# Insiro no valor do dicionario o conteudo 'F'.
        a1_est		= csv_content_dictionary['A1_EST']
        a1_cod_mun	= csv_content_dictionary['A1_COD_MUN']
        a1_cod_mun 	= {k: str(v) for k, v in a1_cod_mun.items()} # Converto tudo para string
        a1_bairro	= csv_content_dictionary['A1_BAIRRO']
        a1_cep		= csv_content_dictionary['A1_CEP']
        a1_cep 	    = {k: str(v) for k, v in a1_cep.items()} # Converto tudo para string

        self.oHelper.SetButton('Incluir')
        for row, a1_cod in enumerate(csv_content_dictionary['A1_COD'].values()):# Percorrer a mesma quantidade do A1_COD na tabela.

            self.oHelper.SetValue('A1_COD', a1_cod2[row])
            self.oHelper.SetValue('A1_LOJA', a1_loja[row])

            self.oHelper.SetValue('A1_PESSOA', a1_pessoa[row])
            self.oHelper.SetValue('A1_NOME', a1_nome[row])
            self.oHelper.SetValue('A1_NREDUZ', a1_nreduz[row])
            self.oHelper.SetValue('A1_END', a1_end[row])
            self.oHelper.SetValue('A1_TIPO', a1_tipo[row])
            self.oHelper.SetValue('A1_EST', a1_est[row])
            self.oHelper.SetValue('A1_COD_MUN', a1_cod_mun[row])
            # Condição para realizar o preenchimento somente se tem conteúdo a ser preenchido neste campo
            if a1_bairro[row].strip(): # strip() é utilizado para remover os espaços em branco da string
                self.oHelper.SetValue('A1_BAIRRO', a1_bairro[row])
            # Condição para realizar o preenchimento somente se tem conteúdo a ser preenchido neste campo
            if a1_cep[row].strip(): # strip() é utilizado para remover os espaços em branco da string
                self.oHelper.SetValue('A1_CEP', a1_cep[row])
            self.oHelper.SetButton('Salvar')
            self.oHelper.AssertTrue()

        self.oHelper.SetButton('Cancelar')

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main() 