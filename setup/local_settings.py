# # type: ignore
# # flake8: noqa

# # Comando:
# # python -c "import string as s;from secrets import SystemRandom as SR;print(''.join(SR().choices(s.ascii_letters + s.digits + s.punctuation, k=64)));"
# SECRET_KEY = 'Gv_v_4uZ35agR)bPEG@m!q&_O~N{[kr<7/Zrd*=,HtGamsp6?h!uMBG6v|M|PR"N'

# # DEBUG DEVE SER False em produção
# DEBUG = False

# # Seu domínio ou IP devem vir aqui
# ALLOWED_HOSTS = [
#     '34.135.148.231',
# ]  # Troque * para seu domínio ou IP

# # Config para postgresql
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'NOME_DA_BASE_DE_DADOS',
#         'USER': 'USUARIO_DA_BASE_DE_DADOS',
#         'PASSWORD': 'SENHA_DA_BASE_DE_DADOS',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }