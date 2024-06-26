**DjangoHW

    Django-проект.

1.
        (19.2)  Создано приложение с названием catalog.
Внесены начальные настройки проекта.
Произведена настройка урлов (URL-файлов) для нового приложения.

        Имеются два шаблона для домашней страницы и страницы с контактной информацией

        В приложении в контроллере реализованы два контроллера:
Контроллер, который отвечает за отображение домашней страницы.
Контроллер, который отвечает за отображение контактной информации,
реализована обработка сбора обратной связи от пользователя,
который зашел на страницу контактов и отправил свои данные для обратной связи

2.      (20.1)
        Подключена СУБД PostgreSQL для работы в проекте, для этого:
Создайте базу данных в ручном режиме.
Внесите изменения в настройки подключения.

        В приложении каталога создайте модели: Product, Category.
Описаны для них начальные настройки.
метод __str__ и class Meta с описанием свойств модели.

        Для каждой модели опишите следующие поля:
Product
        Наименование
        Описание
        Изображение (превью)
        Категория
        Цена за покупку
        Дата создания (записи в БД) created_at
        Дата последнего изменения (записи в БД) updated_at
Category
        Наименование
        Описание
Продукт и Категория связаны, используя связь между таблицами «Один ко многим»
(специальным полем модели — ForeignKey().)
Для поля с изображением добавлены соответствующие настройки (MEDIA URL, MEDIA ROOT, 
настроена URL для отображения медиаданных) в проект, 
а также установлена библиотеку для работы с изображениями Pillow

        Перенесены отображение моделей в базу данных с помощью инструмента миграций, для этого:
созданы миграции для новых моделей;
применены миграции;
внесены изменения в модель продукта, добавлено поле «Дата производства продукта» 
(manufactured_at), применено обновление структуры с помощью миграций;
откат миграции до состояния, когда поле «Дата производства продукта» (manufactured_at) 
для модели продукта еще не существовало, и удалена лишнюя миграция.

        Для моделей категории и продукта настройте отображение в административной панели. 
Для категорий выведите id и наименование в список отображения, 
а для продуктов выведите в список id, название, цену и категорию.
При этом интерфейс вывода продуктов настройте так, чтобы можно было результат отображения 
фильтровать по категории, а также осуществлять поиск по названию и полю описания.

 
        Через инструмент shell заполните список категорий, 
Установите библиотеку ipython для комфортной работы с инструментом shell

        Сформируйте фикстуры для заполнения базы данных.
Фикстуры создайте командой. Для управления кодировкой используйте опцию -Xutf8 для команды. 
Такой параметр уместно будет использовать на операционной системе Windows.
    
        Напишите кастомную команду, которая умеет заполнять данные в базу данных, 
        при этом предварительно ее зачищать от старых данных.

     
        В контроллер отображения главной страницы добавить выборку последних пяти товаров 
        и вывод их в консоль.
        Создать модель для хранения контактных данных и попробовать вывести данные, 
        заполненные через админку, на страницу с контактами.

3.      (20.2)
        Создайте новый контроллер и шаблон, которые будут отвечать за отображение 
        отдельной страницы с товаром, на которой необходимо вывести всю информацию 
        о самом товаре.

        В созданный ранее шаблон для главной страницы выведите список товаров в цикле. 
        Для единообразия выводимых карточек отображаемое описание необходимо обрезать после 
        первых выведенных 100 символов.

        Из-за расширения количества шаблонов появляется слишком много повторяющегося кода, 
поэтому выделите общий (базовый) шаблон, а также подшаблон с главным меню.
В подшаблон вынесите общие для всех кодовые части (HTML-код). 
Не забудьте разместить блок с контентом, куда будут вставляться шаблоны, 
которые используют подшаблон:
{% block content %}
{% endblock %}
И подключите их к другим шаблонам с помощью
{% extends 'путь к базовому шаблону' %}

        Для выводимого изображения на странице реализуйте шаблонный фильтр или шаблонный тег, 
        который преобразует переданный путь в полный путь для доступа к медиафайлу.

        Добавьте функционал создания продукта через внешний интерфейс, созданный вручную.
        Реализуйте постраничный вывод списка продуктов.

4.      (21.1)
        Переведите имеющиеся контроллеры с FBV на CBV.
        
        Создайте новую модель блоговой записи со следующими полями:
заголовок; slug (реализовать через CharField); содержимое;
превью (изображение); дата создания; признак публикации;
количество просмотров.
Для работы с блогом реализуйте CRUD для новой модели.
CRUD реализуйте на основе CBV (ListView, DetailView, CreateView, UpdateView, DeleteView) 

Slug — человекопонятный URL, представляет собой набор символов, которые можно прочитать как 
связные слова или предложения в адресной строке и который служит уникальным идентификатором 
записи в рамках одной модели. Состоит из безопасных для обработки запроса символов:
0–9, a–z (обычно в нижнем регистре) символ -.

        Модифицируйте вывод и обработку запросов, добавив следующую логику на уровне контроллеров:
- При открытии отдельной статьи увеличивать счетчик просмотров.
Для решения этой задачи можно воспользоваться переопределением метода get_object() в DetailView.
- Выводить в список статей только те, которые имеют положительный признак публикации.
Признак публикации — булево поле. Статья может быть опубликована или нет (True/False). 
Отфильтруйте статьи блога с помощью ORM-запроса.
- При создании динамически формировать slug name для заголовка.
Для решения этой задачи можно воспользоваться переопределением метода form_valid() в CreateView.
- После успешного редактирования записи необходимо перенаправлять пользователя на просмотр этой статьи.
Для решения этой задачи можно воспользоваться переопределением метода get_success_url() в UpdateView. 
Метод должен возращать объект reverse с параметрами args.

        Когда статья достигает 100 просмотров, отправлять себе на почту поздравление с достижением.


5.       ДЗ 22.1
         Для модели продуктов реализуйте механизм CRUD, задействовав модуль django.forms.
Условия для пользователей:
могут создавать новые продукты, не могут создавать продукты с запрещенными словами в названии и описании.
Для исключения загрузки запрещенных продуктов реализуйте валидацию названия и описания продукта таким образом, 
чтобы нельзя было в них добавлять слова: казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар.

        Добавьте новую модель «Версия», которая должна содержать следующие поля:
продукт,
номер версии,
название версии,
признак текущей версии.
При наличии активной версии реализуйте вывод в список продуктов информации об активной версии.

        Добавьте реализацию работы с формами для версий продукта.
        Все созданные формы нужно стилизовать так, чтобы они были в единой стилистике оформления всей платформы.

        Дополнительное задание
В один момент может быть только одна активная версия продукта, поэтому при изменении версий необходимо проверять, 
что пользователь в качестве активной версии указал только одну. В случае возникновения ошибки вернуть сообщение 
пользователю и попросить выбрать только одну активную версию.

6.      ДЗ 22.2
        Создайте новое приложения для работы с пользователем. 
Определите собственную форму для пользователя, при этом задайте электронную почту как поле для авторизации.
Также добавьте поля: аватар, номер телефона, страна.
Откат миграции приложения auth (python manage.py migrate auth zero)
        
        В сервисе реализуйте функционал аутентификации, а именно:
- Регистрация пользователя по почте и паролю.
Создайте контроллер для регистрации, 
который будет взаимодействовать с формой регистрации — 
пользователю достаточно ввести почту и пароль.

- Верификация почты пользователя через отправленное письмо.
В контроллере регистрации переопределите метод form_valid()
 и встройте автоматическую отправку электронного сообщения пользователю 
на указанный в форме регистрации адрес.
  (Для отправки электронной почты воспользуйтесь встроенной в Django функцией 
send_mail().)

- Авторизация пользователя.
Создайте отдельный контроллер для авторизации (LoginView) и зарегистрируйте его в приложении.

- Восстановление пароля зарегистрированного пользователя на автоматически сгенерированный пароль.
Создайте новый контроллер для восстановления пароля.
В интерфейсе кнопка «Восстановить пароль» должна отображаться на странице входа.
Пользователь вводит адрес электронной почты, в контроллере происходит генерация пароля, 
перезапись пароля для пользователя с соответсвующим адресом электронной почты и отправка 
сообщения с новым паролем на адрес почты. (Пароль можно сгенерировать с помощью библиотеки 
random.). Помните, что пароль в базе данных хранится в захешированном виде. 
Для установки пароля пользователю можно воспользоваться функцией make_password()

        Все контроллеры, которые отвечают за работу с продуктами, 
        закройте для анонимных пользователей, при этом создаваемые 
        продукты должны автоматически привязываться к авторизованному пользователю.

Чтобы закрыть контроллеры от анонимных пользователей, добавьте в CBV-контроллеры дополнительное наследование от 
LoginRequiredMixin. Не забудьте добавить поле для продуктов, которое будет указывать на владельца. 
Оно должно быть ссылкой на модель пользователя.
Для автоматической привязки пользователя к продукту переопределите в контроллере создания продукта метод 
form_valid(). Текущий авторизованный пользователь доступен через self.request.user 
 — запишите его в только что созданный продукт и не забудьте сохранить объект в базу данных.

        Дополнительное задание
Добавьте интерфейс редактирования профиля пользователя.

        ДЗ (23.2)
    Создайте группу для роли модератора и опишите необходимые доступы:
может отменять публикацию продукта,
может менять описание любого продукта,
может менять категорию любого продукта.
(Недостающее поле признака публикации необходимо добавить таким образом, 
чтобы можно было определять статус продукта. Можно использовать 
BooleanField со значением False по умолчанию или CharField с указанием 
вариантов значений (choises). При этом по умолчанию должен быть вариант, 
который не предполагает публикации продукта.

    Реализуйте решение, которое проверит, что редактирование продукта доступно только его владельцу.
Внедрите в шаблоны проверку на владельца объекта и отображайте кнопки редактирования только пользователям, 
которые являются владельцами (если пользователь не наделен другими правами).
 
    Дополнительное задание
Выделите отдельную роль для пользователя — контент-менеджера, который может управлять публикациями в блоге. 
Также не забудьте реализовать проверки на то, что обычный пользователь или 
модератор из другого отдела не сможет ничего изменить в разделе блога.


7.        ДЗ 23.1
        1.Установите брокер для кеширования Redis. 
Настройки в проекте для Ubuntu/Linux. 
Redis доступен для использования по адресу 127.0.0.1:6379, если вы не меняли порт для запуска. 

        2.Настройте кеширование всего контроллера отображения данных относительно одного продукта.
Кеширование подключено в файле маршрутизации urls.py. 

        3.Создана сервисная функция, которая отвечает за выборку категорий 
        и которую можно переиспользовать в любом месте системы. 
        Добавлено низкоуровневое кеширование для списка категорий.

Реализован контроллер и шаблон для выдачи списка категорий 
переопределена get_queryset (на возврат результата работы данной функции.)
возможно в качестве контекста передавать результат работы этой функции (закомментирован)

        4.Вынесите необходимые настройки в переменные окружения и настройте проект для работы с ними.
Для работы с проектом необходимо создать файл .env, пример его заполнения есть в проекте в файле .env.sample
(в файле .env должны быть размещены все чувствительные данные, которые хранятся в настройках приложения: 
секретный ключ Django, настройки базы данных, настройки кеширования (адрес подключения к брокеру, включение кеширования), 
включение режима отладки и любые логины и пароли от сторонних сервисов, например данные учетной записи для отправки почты. 
Любые данные, которые могут при утечке навредить вашему приложению и являются чувствительными.)

            Дополнительное задание
Добавлено кеширование всего сайта целиком, при этом отключены от кеширования контроллеры, 
которые отвечают за работу по заполнению продуктов и блога.
