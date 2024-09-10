# Define todos os personagens do jogo
define nvl_nar = Character(None, kind=nvl, what_color = "#ffffff")

define a = Character("Anna", color="#f2c94c", image="a" ,what_prefix='"', what_suffix='"',  who_outlines=[(absolute(2), "#352f36", absolute(1), absolute(1))])
image a = "anna_neutro"
image a feliz = "anna_feliz"
image a triste = "anna_triste"
image a brava = "anna_brava"

define chefe = Character("Chefe", color="#d84444", what_prefix='"', what_suffix='"',  who_outlines=[(absolute(2), "#352f36", absolute(1), absolute(1))])
define e = Character("Editor", color="#b04cf2", what_prefix='"', what_suffix='"',  who_outlines=[(absolute(2), "#352f36", absolute(1), absolute(1))])

define t = Character("Anthony", color="#46aa63", what_prefix='"', what_suffix='"',  who_outlines=[(absolute(2), "#352f36", absolute(1), absolute(1))])
define s = Character("Segurança", color="#6cc4f7", what_prefix='"', what_suffix='"',  who_outlines=[(absolute(1), "#352f36", absolute(0), absolute(0))])
define quem = Character("???", color="#000000ff", what_prefix='"', what_suffix='"',  who_outlines=[(absolute(1), "#ffffff", absolute(0), absolute(0))])