from behave import *
from nose.tools import assert_equal
from page.caed_page import caedPage

caed_page = caedPage()

@given(u'Acesso a pagina oficial do Caed')
def step_impl(context):
    caed_page.acess_page(url="http://www.caed.ufjf.br/")



@then(u'abrir a pagina')
def step_impl(context):
   caed_page.send_keys_input_pesquisa()