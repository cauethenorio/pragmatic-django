import pytest
from reusable_app.models import UserChange


def test_user_creation_registration(db, user_factory):
    user1, user2 = user_factory.create_batch(2)

    assert UserChange.objects.count() == 2
    assert UserChange.objects.filter(action_type=UserChange.ActionType.CREATED).count() == 2
    assert UserChange.objects.filter(user=user1).count() == 1
    assert UserChange.objects.filter(user=user2).count() == 1


def test_user_update_registration(db, user_factory):
    user1, user2 = user_factory.create_batch(2)
    # assets just one UserChange instance exists
    num_changes = UserChange.objects.count()

    user1.email = "somethingelse@example.com"
    user1.save()

    assert UserChange.objects.count() == num_changes + 1
    user_update_change = UserChange.objects.filter(
        action_type=UserChange.ActionType.UPDATED
    ).get()
    assert user_update_change.user.pk == user1.pk


def test_user_deletion_registration(db, user):
    user_pk = user.pk
    num_changes = UserChange.objects.count()
    user.delete()

    assert UserChange.objects.count() == num_changes + 1
    assert UserChange.objects.filter(
        action_type=UserChange.ActionType.DELETED
    ).get().deleted_user_id == user_pk


@pytest.mark.parametrize(
    'action_type', (
        UserChange.ActionType.CREATED,
        UserChange.ActionType.UPDATED,
        UserChange.ActionType.DELETED,
    )
)
def test_user_changes_should_be_kept_on_user_deletion(db, user, action_type):
    user.first_name = 'Marry'
    user.save()
    user_pk = user.pk
    user.delete()

    assert UserChange.objects.filter(
        action_type=action_type,
        deleted_user_id=user_pk
    ).count() == 1