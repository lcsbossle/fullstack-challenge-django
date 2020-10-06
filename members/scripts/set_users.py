from django.contrib.auth.models import Group, User, Permission

professor_group, prof_created = Group.objects.get_or_create(name='Professor')
aluno_group, al_created = Group.objects.get_or_create(name='Aluno')

aluno_user = User.objects.create_user(
    'Aluno',
    'aluno@empresa.com.br',
    'alunosenha'
    )

aluno_user.first_name = 'Chaves'
aluno_user.last_name = 'Da Vila'
aluno_user.save()
aluno_user.groups.add(aluno_group)

prof_user = User.objects.create_user(
    'Professor',
    'professor@empresa.com.br',
    'profesenha'
    )

prof_user.first_name = 'Inocencio'
prof_user.last_name = 'Girafales'
prof_user.save()
prof_user.groups.add(professor_group)

prof_permissions_names = [
    'Can add aula',
    'Can change aula',
    'Can delete aula',
    'Can view aula',
    'Can add curso',
    'Can change curso',
    'Can delete curso',
    'Can view curso',
    'Can add sequencia',
    'Can change sequencia',
    'Can delete sequencia',
    'Can view sequencia',
]

prof_permissions = []
for p in prof_permissions_names:
    prof_permissions.append(Permission.objects.get(name=p))

alumni_permission_names = [
    'Can view aula',
    'Can view curso',
    'Can view sequencia',
]

alumni_permissions = []
for p in alumni_permission_names:
    alumni_permissions.append(Permission.objects.get(name=p))

professor_group.permissions.set(prof_permissions)
aluno_group.permissions.set(alumni_permissions)