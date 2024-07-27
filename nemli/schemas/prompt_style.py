from types import MappingProxyType

PARTICIPANTS = "e descrevendo a participação de cada usuário."
EXTRA = "Agrupe os assuntos por atos e cenas, relacionando os assuntos com os usuários que participaram da discussão."

prompt_types = MappingProxyType(
    {
        "padrão": f"Resuma a seguinte conversa por assuntos, agrupando por similaridade {PARTICIPANTS}",
        "novela mexicana": (
            "Resuma a seguinte conversa, estruturando como um roteiro de novela mexicana (Maria do Bairro)"
            f" {PARTICIPANTS} {EXTRA} Lembre-se de adicionar muitos dramas, reviravoltas e seja bem exacerbado."
        ),
        "terror": (
            "Resuma a seguinte conversa, estruturando como um roteiro de filme de suspense/terror"
            f" {PARTICIPANTS} {EXTRA} Lembre-se de adicionar muito suspense e drama."
        ),
        "faroeste": (
            "Resuma a seguinte conversa, estruturando como um roteiro de filme de velho oeste americano"
            f" {PARTICIPANTS}. {EXTRA} Lembre-se de adicionar muitos tiroteios e duelos."
        ),
        "star wars": (
            "Resuma a seguinte conversa, estruturando como um roteiro de um episódio / filme de Star Wars"
            f" {PARTICIPANTS}. {EXTRA} Lembre-se de adicionar muitas batalhas espaciais e duelos."
        ),
        "senhor dos anéis": (
            "Resuma a seguinte conversa, estruturando como um roteiro de filme ou livro do Senhor dos Anéis"
            f" {PARTICIPANTS}. {EXTRA} Lembre-se de adicionar muitas batalhas épicas e aventuras."
        ),
        "cyberpunk": (
            "Resuma a seguinte conversa, estruturando como um roteiro de filme de cyberpunk / sci-fi / futurista"
            f" {PARTICIPANTS}. {EXTRA} Lembre-se de adicionar muita tecnologia, neon e cenas de ação."
        ),
        "ursinho carinhoso": (
            "Resuma a seguinte conversa, estruturando como um roteiro de desenho animado dos Ursinhos Carinhosos"
            f" {PARTICIPANTS}. {EXTRA} Lembre-se de adicionar muita fofura e amor (o amor venceu!)."
        ),
    }
)
