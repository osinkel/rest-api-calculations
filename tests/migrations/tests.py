from pytest_alembic import tests, create_alembic_fixture

history = create_alembic_fixture({"file": "alembic.ini"})


def test_single_head_revision_history(history):
    tests.test_single_head_revision(history)


def test_upgrade_history(history):
    tests.test_upgrade(history)


# This test is for autogeneration migrations
# def test_model_definitions_match_ddl_history(history):
#     tests.test_model_definitions_match_ddl(history)


def test_up_down_consistency_history(history):
    tests.test_up_down_consistency(history)
