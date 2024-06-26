from dataclasses import dataclass
@dataclass
class Admin:
    id:int
    name:str
    user_name:str
@dataclass
class Bot:
    id:int
    name:str
    user_name:str
    token:str
    db:str
@dataclass
class SisAdmin:
    id:int
    name:str
    user_name:str
@dataclass
class Paterns:
    bot:Bot
    admin:Admin
    sisadmin:SisAdmin
def get_paterns() -> Paterns:
    return Paterns(
        bot=Bot(
            id=0,
            name="AutoSchool",
            user_name="AutoSchool_uz_bot",
            token="6297301326:AAE8kC3JLIF_ZXNA07Zcj-byBUkq2ru7TI0",
            db='bot.db'
            ),
        admin=Admin(
            id=5486903240,#438039439,
            name="Dilmurod",
            user_name="mahkamovdilmurod",
        ),
        sisadmin=SisAdmin(
            id=5486903240,
            name="Asadbek",
            user_name="asadbek_hikmatullayev"
        )
    )
patern:Paterns = get_paterns()