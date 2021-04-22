from typing import List, Dict

NUMBER_SOUND_MAPPINGS = {3: "Pling", 5: "Plang", 7: "Plong"}


def convert(number: int) -> str:
    sound_waves: List[str] = []

    for number_key, sound  in NUMBER_SOUND_MAPPINGS.items():
        if number % number_key == 0:
            sound_waves.append(sound)

    return "".join(sound_waves) if sound_waves else str(number)
