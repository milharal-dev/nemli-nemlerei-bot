from types import MappingProxyType

EXTRA = "Agrupe os assuntos por atos e cenas, relacionando os assuntos com os usuários que participaram da discussão."

prompt_types = MappingProxyType(
    {
        "padrão": (
            "Resuma a seguinte conversa por assuntos, agrupando por similaridade e descrevendo a participação de"
            " cada usuário."
        ),
        "novela mexicana": (
            "Resuma a seguinte conversa, estruturando como um roteiro de novela mexicana (Maria do Bairro)."
            f" {EXTRA}"
            " Lembre-se de adicionar muitos dramas, reviravoltas e seja bem exacerbado."
        ),
        "terror": (
            f"Resuma a seguinte conversa, estruturando como um roteiro de filme de suspense/terror. {EXTRA}"
            " Lembre-se de adicionar muito suspense e drama."
        ),
        "faroeste": (
            f"Resuma a seguinte conversa, estruturando como um roteiro de filme de velho oeste americano. {EXTRA}"
            " Lembre-se de adicionar muitos tiroteios e duelos."
        ),
    }
)
