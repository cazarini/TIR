from tir import Webapp

test_helper = Webapp()
test_helper.Setup('SIGAFAT','20/12/2021','99','01','05')
test_helper.Program('MATA030')
test_helper.SetButton('Incluir')

test_helper.SetValue('A1_COD','000001')
test_helper.SetValue('A1_LOJA','01')

test_helper.SetButton('Confirmar')

test_helper.TearDown()
