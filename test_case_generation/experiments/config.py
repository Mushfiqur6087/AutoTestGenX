from pathlib import Path

MODELS = {
    "gpt-4o-mini": {
        "model":       "openai/gpt-4o-mini",
        "api_key_env": "OPENAI_API_KEY",
        "rpm":         500,
    },
    "gpt-5-mini": {
        "model":       "openai/gpt-5-mini",
        "api_key_env": "OPENAI_API_KEY",
        "rpm":         500,
    },
}

SPECS = {
    "SwagLab": {
        "spec":            "dataset/raw_specifications/SwagLab/SwagLab.md",
        "few_shot_prompt": "baselines/few_shot/SwagLab_few_shot.md",
        "existing_agent": {
            "gpt-5-mini":  None,
            "gpt-4o-mini": None,
        },
    },
    "Mifos": {
        "spec":            "dataset/raw_specifications/Mifos/Mifos.md",
        "few_shot_prompt": "baselines/few_shot/Mifos_few_shot.md",
        "existing_agent": {
            "gpt-5-mini":  "outputs/test_case_generation/Mifos/openai-gpt-5-mini",
            "gpt-4o-mini": None,
        },
    },
    "Parabank": {
        "spec":            "dataset/raw_specifications/Parabank/Parabank.md",
        "few_shot_prompt": "baselines/few_shot/Parabank_few_shot.md",
        "existing_agent": {
            "gpt-5-mini":  "outputs/test_case_generation/Parabank/openai-gpt-5-mini",
            "gpt-4o-mini": None,
        },
    },
    "PHPTravels": {
        "spec":            "dataset/raw_specifications/PHPTravels/PHPTravels.md",
        "few_shot_prompt": "baselines/few_shot/PHPTravels_few_shot.md",
        "existing_agent": {
            "gpt-5-mini":  "outputs/test_case_generation/Phptravels/openai-gpt-5-mini",
            "gpt-4o-mini": None,
        },
    },
    "MoodleTeacher": {
        "spec":            "dataset/raw_specifications/Moodle/MoodleTeacher.md",
        "few_shot_prompt": "baselines/few_shot/MoodleTeacher_few_shot.md",
        "existing_agent": {
            "gpt-5-mini":  "outputs/test_case_generation/Moodleteacher/openai-gpt-5-mini",
            "gpt-4o-mini": None,
        },
    },
    "MoodleStudent": {
        "spec":            "dataset/raw_specifications/Moodle/MoodleStudent.md",
        "few_shot_prompt": "baselines/few_shot/MoodleStudent_few_shot.md",
        "existing_agent": {
            "gpt-5-mini":  "outputs/test_case_generation/Moodlestudent/openai-gpt-5-mini",
            "gpt-4o-mini": None,
        },
    },
}

ZERO_SHOT_PROMPT_PATH = "baselines/zero_shot/prompt.md"
RESULTS_DIR = Path("results")
