class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    return user in group.get_users()


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print("Pass: is_user_in_group(sub_child_user, sub_child) = " + str(is_user_in_group(sub_child_user, sub_child))
      if is_user_in_group(sub_child_user, sub_child) else
      "Fail: is_user_in_group(sub_child_user, sub_child) != " + str(is_user_in_group(sub_child_user, sub_child)))

print("Pass: is_user_in_group(sub_child_user, child) = " + str(is_user_in_group(sub_child_user, child))
      if not is_user_in_group(sub_child_user, child) else
      "Fail: is_user_in_group(sub_child_user, child) != " + str(is_user_in_group(sub_child_user, child)))

print("Pass: is_user_in_group(sub_child_user, parent) = " + str(is_user_in_group(sub_child_user, parent))
      if not is_user_in_group(sub_child_user, parent) else
      "Fail: is_user_in_group(sub_child_user, parent) != " + str(is_user_in_group(sub_child_user, parent)))
