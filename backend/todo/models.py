from django.db import models

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, verbose_name="Название")

    class Meta:
        managed = True
        db_table = 'todo_auth_group'  # Добавлен префикс todo_
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return self.name


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING, verbose_name="Группа")
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING, verbose_name="Разрешение")

    class Meta:
        managed = True
        db_table = 'todo_auth_group_permissions'  # Добавлен префикс todo_
        unique_together = (('group', 'permission'),)
        verbose_name = "Разрешение группы"
        verbose_name_plural = "Разрешения групп"

    def __str__(self):
        return f"{self.group} - {self.permission}"


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, verbose_name="Тип контента")
    codename = models.CharField(max_length=100, verbose_name="Кодовое имя")

    class Meta:
        managed = True
        db_table = 'todo_auth_permission'  # Добавлен префикс todo_
        unique_together = (('content_type', 'codename'),)
        verbose_name = "Разрешение"
        verbose_name_plural = "Разрешения"

    def __str__(self):
        return self.name


class AuthUser(models.Model):
    password = models.CharField(max_length=128, verbose_name="Пароль")
    last_login = models.DateTimeField(blank=True, null=True, verbose_name="Последний вход")
    is_superuser = models.IntegerField(verbose_name="Суперпользователь")
    username = models.CharField(unique=True, max_length=150, verbose_name="Имя пользователя")
    first_name = models.CharField(max_length=30, verbose_name="Имя")
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    email = models.CharField(max_length=254, verbose_name="Email")
    is_staff = models.IntegerField(verbose_name="Персонал")
    is_active = models.IntegerField(verbose_name="Активен")
    date_joined = models.DateTimeField(verbose_name="Дата регистрации")

    class Meta:
        managed = True
        db_table = 'todo_auth_user'  # Добавлен префикс todo_
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, verbose_name="Пользователь")
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING, verbose_name="Группа")

    class Meta:
        managed = True
        db_table = 'todo_auth_user_groups'  # Добавлен префикс todo_
        unique_together = (('user', 'group'),)
        verbose_name = "Группа пользователя"
        verbose_name_plural = "Группы пользователей"

    def __str__(self):
        return f"{self.user} - {self.group}"


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, verbose_name="Пользователь")
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING, verbose_name="Разрешение")

    class Meta:
        managed = True
        db_table = 'todo_auth_user_user_permissions'  # Добавлен префикс todo_
        unique_together = (('user', 'permission'),)
        verbose_name = "Разрешение пользователя"
        verbose_name_plural = "Разрешения пользователей"

    def __str__(self):
        return f"{self.user} - {self.permission}"


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField(verbose_name="Время действия")
    object_id = models.TextField(blank=True, null=True, verbose_name="ID объекта")
    object_repr = models.CharField(max_length=200, verbose_name="Представление объекта")
    action_flag = models.PositiveSmallIntegerField(verbose_name="Флаг действия")
    change_message = models.TextField(verbose_name="Сообщение об изменении")
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True, verbose_name="Тип контента")
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, verbose_name="Пользователь")

    class Meta:
        managed = True
        db_table = 'todo_django_admin_log'  # Добавлен префикс todo_
        verbose_name = "Журнал администрирования"
        verbose_name_plural = "Журналы администрирования"

    def __str__(self):
        return f"{self.action_time} - {self.user}"


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, verbose_name="Метка приложения")
    model = models.CharField(max_length=100, verbose_name="Модель")

    class Meta:
        managed = True
        db_table = 'todo_django_content_type'  # Добавлен префикс todo_
        unique_together = (('app_label', 'model'),)
        verbose_name = "Тип контента"
        verbose_name_plural = "Типы контента"

    def __str__(self):
        return f"{self.app_label} - {self.model}"


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, verbose_name="Приложение")
    name = models.CharField(max_length=255, verbose_name="Название")
    applied = models.DateTimeField(verbose_name="Применено")

    class Meta:
        managed = True
        db_table = 'todo_django_migrations'  # Добавлен префикс todo_
        verbose_name = "Миграция"
        verbose_name_plural = "Миграции"

    def __str__(self):
        return f"{self.app} - {self.name}"


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, verbose_name="Ключ сессии")
    session_data = models.TextField(verbose_name="Данные сессии")
    expire_date = models.DateTimeField(verbose_name="Дата истечения")

    class Meta:
        managed = True
        db_table = 'todo_django_session'  # Добавлен префикс todo_
        verbose_name = "Сессия"
        verbose_name_plural = "Сессии"

    def __str__(self):
        return self.session_key


class Todo(models.Model):
    title = models.CharField(max_length=120, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    completed = models.IntegerField(verbose_name="Завершено")

    class Meta:
        managed = True
        db_table = 'todo_todo'  # Добавлен префикс todo_
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.title


class TodoUser(models.Model):
    username = models.CharField(max_length=30, blank=True, null=True, verbose_name="Имя пользователя")
    password = models.CharField(max_length=30, blank=True, null=True, verbose_name="Пароль")

    class Meta:
        managed = True
        db_table = 'todo_todo_user'  # Добавлен префикс todo_
        verbose_name = "Пользователь задачи"
        verbose_name_plural = "Пользователи задач"

    def __str__(self):
        return self.username if self.username else "Без имени"