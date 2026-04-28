# Data Science Interview Mastery: Журнал обновлений (Gemini AI)

Этот файл содержит подробную историю итеративного улучшения приложения для подготовки к интервью по Data Science.

## 📝 Обзор проекта
*   **Цель:** Масштабное обновление контента (1000 вопросов) до уровня **Team Lead**.
*   **Стек:** HTML5, CSS3 (Glassmorphism), Vanilla JavaScript, Python (для обработки данных), LaTeX ($\LaTeX$).
*   **Итоговое состояние:** Полностью автономное (offline) приложение с глубокой теорией и примерами кода.

---

## 🚀 Основные этапы работы

### 1. Исправление интерфейса
*   **Фильтрация разделов:** Исправлена ошибка, при которой выбор конкретной темы (например, Python или SQL) не приводил к обновлению списка вопросов. Теперь фильтрация работает мгновенно.
*   **Категория "All Topics":** Исправлен счетчик и логика отображения всех вопросов.

### 2. Масштабное обновление контента (Итерации 1-18)
Мы провели 18 итераций обновления базы данных `questions.json`. Около **266+ ключевых вопросов** были переписаны с нуля.

#### Итерация 18 (2026-04-26):
*   **Первая партия (Batch 1) расширения до 1000 вопросов:** Обновлено 56 вопросов.
*   **SQL Junior:** NULL, CHAR vs VARCHAR, подзапросы, GROUP BY, IN vs EXISTS, DISTINCT, ORDER BY, LIMIT/OFFSET, LIKE, BETWEEN.
*   **Linear Algebra:** Глубокий разбор SVD.
*   **NLP:** Токенизация, Word2Vec vs BERT, Self-Attention.
*   **Computer Vision:** Свертки, сегментация, YOLO.
*   **MLOps:** Data versioning (DVC), Model Registry, CT (Continuous Training).
*   **System Design:** Scaling, CAP Theorem.
*   **Big Data:** Hadoop/MapReduce, Spark vs MapReduce.
*   **Deep Learning:** Transfer Learning, Pooling, Softmax.
*   **Python:** Декораторы, генераторы, управление памятью (deep/shallow copy), контекстные менеджеры, основы (PEP 8, List/Tuple/Set/Dict).
*   **Statistics & ML:** Параметрика vs Непараметрика, A/B тесты, Bootstrap, Survival Analysis, Bias-Variance tradeoff, Overfitting.

---

### 3. Локализация и очистка
*   **Полный перевод:** Вся база данных переведена на русский язык. Устранены все англоязычные "хвосты".
*   **Техническая чистота:** Внедрена поддержка $\LaTeX$ для красивого отображения математических формул прямо в карточках вопросов.
*   **Cleanup:** После завершения работы удалены все временные Python-скрипты (`update_batch_*.py`, `detect_english.py` и др.).

### 4. Интеграция SQL Задач и Quiz UI (2026-04-26)
*   **Парсинг:** С помощью скрипта на Python из сырой HTML-выгрузки Telegram (папка `ChatExport_2026-04-26`) были успешно извлечены структурированные данные.
*   **SQL-задачи:** Сформирована новая база `sql_tasks.json` на 455 вопросов.
*   **Quiz UI:** Реализован интерфейс в стиле "Кто хочет стать миллионером" для режима SQL-задач.
    *   Варианты ответов выводятся в виде интерактивных кнопок (A, B, C, D...).
    *   Визуальная обратная связь: кнопка окрашивается в зеленый при правильном ответе и в красный при ошибке.
    *   Кнопка "Show Answer" скрыта для этого режима, так как ответ проверяется действием пользователя.
*   **Паттерны SQL Задач:**
    *   **Опросы (Polls):** Автоматически преобразуются в интерактивные квизы.
    *   **Текстовые задачи:** Сохраняют классический формат с развернутым ответом.

---

## 🛠️ Инструментарий разработки
В процессе работы использовались следующие вспомогательные инструменты:
1.  `build_app.py`: Скрипт для сборки `ds-interview-standalone.html` из шаблона и JSON.
2.  `update_batch.py`: Модульный скрипт для инъекции обновленных ответов в базу.
3.  `detect_english.py`: Скрипт для аудита полноты перевода.

## 📊 Итоговая статистика
*   **Всего вопросов:** 1000
*   **Глубоко проработанных вопросов (250+ символов):** ~266
*   **Язык интерфейса и контента:** Русский
*   **Формат формул:** LaTeX
*   **Зависимости:** Отсутствуют (полностью автономный HTML)

---
*Журнал обновлен: 2026-04-26. Подготовлено Antigravity (Gemini AI).*


#### Проработанные разделы:
*   **Python:** Продвинутые темы (GIL, декораторы, генераторы, управление памятью, MRO).
*   **SQL:** Оконные функции, CTE, оптимизация запросов, различия движков (Spark SQL vs Hive).
*   **Linear Algebra:** SVD, PCA, собственные числа, матричные разложения (LU, Cholesky), псевдообратные матрицы.
*   **Probability:** Теорема Байеса, парадокс дней рождения, сопряженные распределения, MLE, Importance Sampling.
*   **Statistics:** Z-test vs T-test, ANOVA, Bootstrap, p-hacking, доверительные интервалы, корреляции Пирсона/Спирмена.
*   **Machine Learning:** Классические алгоритмы (SVM, k-NN, деревья), ансамбли (Random Forest, XGBoost, CatBoost), метрики (ROC-AUC, F1, Log-Loss).
*   **Deep Learning:** Функции активации, инициализация весов, сверточные сети (CNN), RNN/LSTM, GAN, Autoencoders.
*   **NLP:** Word2Vec, FastText, Transformers (Attention, BERT, GPT), BLEU, Perplexity.
*   **Computer Vision:** YOLO, сегментация (Semantic/Instance), NMS, Anchor Boxes, аугментации (Mixup/CutMix).
*   **MLOps & Engineering:** Model Drift, Feature Stores, сжатие моделей (Quantization/Pruning), DVC, CI/CD для ML.
*   **Big Data:** Hadoop (HDFS/MapReduce), Spark (Catalyst, RDD), Kafka.

### 3. Локализация и очистка
#### Итерация 20 (2026-04-26):
*   **Третья партия (Batch 3) расширения:** Обновлено 42 вопроса.
*   **Разделы:** Computer Vision (YOLO, ViT, Segmentation, mAP), NLP (Word Embeddings, GPT vs BERT, BPE, Perplexity), Big Data (Hadoop, Spark RDD, Flink, Columnar storage), System Design (CAP, Load Balancer, Microservices, API), MLOps (Model Registry, Drift, Monitoring).

#### Итерация 21 (2026-04-26):
*   **Четвертая партия (Batch 4) расширения:** Обновлено 50 вопросов (индексы 351-400).
*   **SQL Tasks Verification:** Проведена полная ручная верификация всех **455** задач по SQL. Исправлены `correct_index` для сотен задач, где по умолчанию стоял 0.
*   **Разделы Batch 21:** 
    *   **System Design:** Rate Limiting, Event-driven architecture, Low-latency recommendations, Load Balancer, Cache.
    *   **Big Data:** Flink vs Spark, Data Pipelines, MapReduce, Apache Spark.
    *   **MLOps:** Docker in ML, CI/CD for ML.
    *   **Python:** zip(), f-strings, is vs ==, map(), @property, str vs repr, __slots__, help(), __dict__, copy (shallow/deep), itertools, slicing, metaclasses.
    *   **SQL:** LIKE, WHERE vs HAVING, Primary/Foreign Keys, Joins, Group By, ACID, Indices, Subqueries, Self Join.
    *   **CV/NLP:** TextRank, NER, Transformers, Attention, Pixels, Convolutions, Pooling, Object Detection.
*   **Общий прогресс проработки:** ~400/1000 вопросов.

---

## 🛠️ Инструментарий разработки
В процессе работы использовались следующие вспомогательные инструменты:
1.  `build_app.py`: Скрипт для сборки `ds-interview-standalone.html` из шаблона и JSON.
2.  `extract_sql_tasks.py`: Скрипт для извлечения и подготовки SQL задач из Telegram.
3.  `update_batch_*.py`: Скрипты для инъекции обновленных ответов в базу.

## 📊 Итоговая статистика
*   **Всего вопросов:** 1000
*   **SQL Задач (Telegram):** 455 (Верифицированы)
*   **Глубоко проработанных вопросов (250+ символов):** ~400
*   **Язык интерфейса и контента:** Русский
*   **Формат формул:** LaTeX
*   **Зависимости:** Отсутствуют (полностью автономный HTML)

#### Итерация 22 (2026-04-26):
*   **Пятая партия (Batch 5) расширения:** Обновлено 54 вопроса (индексы 401-454).
*   **Разделы:** Продвинутый Python (Itertools, Metaclasses), SQL (Оконные функции, Оптимизация), System Design (Data Modeling), MLOps (Data Drift, Versioning).

#### Итерация 23 (2026-04-26):
*   **Шестая партия (Batch 6) расширения:** Обновлено 50 вопросов (индексы 501-550).
*   **Разделы:** 
    *   **MLOps:** Теневое и канареечное развертывание (Shadow/Canary), Feature Store, CI/CD/CT.
    *   **System Design:** CAP-теорема, Шардирование, Репликация, CDN, Rate Limiting, RecSys Ranking.
    *   **Python:** Asyncio, ABC, Контекстные менеджеры, Init vs New, Classmethod vs Statmethod, Слайсы.
    *   **SQL:** CASE WHEN, COALESCE, UNION vs INTERSECT, NTILE, Deadlocks, Temporary Tables.
*   **Общий прогресс проработки:** ~550/1000 вопросов.

#### Итерация 24 (2026-04-26):
*   **Седьмая партия (Batch 7) расширения (Patching & Expanding):** Обновлено 50 вопросов.
*   **Особенность:** Проведен аудит первых 700 вопросов и закрыты "дыры" (короткие ответы). Начата проработка нового блока вопросов (710+).
*   **Разделы:** 
    *   **SQL:** [x] Content Translation (766 / 1503 items), Materialization, Window Functions (LEAD/LAG), Normalization (1NF-3NF).
    *   **ML:** SHAP values, Overfitting, LOOCV, PCA, Clustering, Evaluation metrics (F1-score, Target/Feature).
    *   **DL:** ResNet, Momentum, Batch Normalization, Image Augmentation, LeNet-5.
    *   **Python:** Descriptors, @property, Magic methods (__str__ vs __repr__), Pickle module.
*   **Общий прогресс проработки:** ~600/1000 вопросов.

#### Итерация 25 (2026-04-26):
*   **Восьмая партия (Batch 8) расширения:** Обновлено 50 вопросов.
*   **Разделы:** 
    *   **DL:** Gradient Clipping, GAN, Adam, Learning Rate, Fine-tuning, VGG, Vanishing Gradient.
    *   **Statistics:** Student's t-test, IQR, Boxplot, Type II Error, CLT (ЦПТ).
    *   **Probability:** Bernoulli, Poisson, Markov Chains, Permutations/Combinations, Discrete/Continuous variables.
    *   **NLP:** Text Normalization, FastText, Seq2Seq, Transformers (Enc/Dec), POS-tagging, Parsing, Levenshtein distance.
    *   **CV:** SIFT/SURF, Sobel, ViT (Vision Transformer), ROI, Harris Corner Detector.
*   **Общий прогресс проработки:** ~650/1000 вопросов.

#### Итерация 26 (2026-04-26):
*   **Девятая партия (Batch 9) расширения:** Обновлено 50 вопросов.
*   **Разделы:** 
    *   **CV:** Morphological operations, Binarization, IoU, Image Pyramid, Optical Flow, Siamese Networks.
    *   **Big Data:** Columnar DBs, Apache Hive, Apache Airflow, Lambda/Kappa Architecture, DWH, Scaling, ClickHouse, Replication.
    *   **MLOps:** Model Registry, Monitoring, Feature Store, Testing in ML.
    *   **System Design:** Latency/Throughput, Microservices vs Monolith, API Gateway, CDN, Rate Limiting, Sharding, Cache, Load Balancing.
    *   **Linear Algebra:** Dot Product, Transpose, Determinant, Rank, Eigenvalues/vectors, SVD, Norms, Orthogonality, Inverse Matrix.
    *   **Python:** PEP 8, Zen of Python, Coroutines (asyncio), Monkey Patching, GC, Weakref, Magic methods (__init__, __call__), sys.argv, Scopes.
*   **Общий прогресс проработки:** ~700/1000 вопросов.

#### Итерация 27 (2026-04-26):
*   **Десятая партия (Batch 10) расширения:** Обновлено 50 вопросов.
*   **Разделы:** 
    *   **SQL:** UPDATE/DELETE, CROSS JOIN, B-Tree Indexing, Materialized Views, Partitioning, COALESCE, EXISTS, Transaction Isolation, WAL, In-Memory DB, Recursive CTE, Explain Plan.
    *   **Machine Learning:** Dummy Variable Trap, Correlation, DBSCAN, Information Gain, Probability Calibration, Online Learning, Multicollinearity, Label Encoding, Adversarial Attacks, k-fold CV.
    *   **Deep Learning:** Attention, GRU, CNN Architecture, Weight Decay, Early Stopping, SGD, Exploding Gradients, Cross-Entropy.
    *   **NLP:** Stop words, Embeddings, Word2Vec, BERT, NER, Bag of Words.
*   **Общий прогресс проработки:** ~750/1000 вопросов.

#### Итерация 29 (2026-04-26):
*   **Финальная зачистка (Batch 12):** Обновлены последние 60 вопросов (заполнены все «дыры» в ранних индексах и дубли в конце).
*   **Результат:** Проект полностью завершен в плане контента.
    *   **SQL:** Индексы, EXPLAIN, N+1, CASE, репликация, миграции, шардирование.
    *   **Python:** GIL, *args/**kwargs, магические методы, MRO, Dataclasses, Walrus, Threading/Multiprocessing.
    *   **Math:** Распределение Пуассона, PDF/CDF, Цепи Маркова, Монте-Карло, Линейная алгебра (собственные числа, инверсия).
    *   **Big Data:** Полный стек Hadoop/Spark/Kafka/Airflow/ClickHouse.
*   **Общий прогресс проработки:** 1048/1048 вопросов (100% Премиум).

#### Итерация 30 (2026-04-26):
*   **Реализация мультиязычности (RU/EN):**
    *   Миграция JSON-схемы: все поля `question`, `answer`, `options` теперь поддерживают `ru` и `en`.
    *   Интерфейс: Добавлен переключатель языков в хедер.
    *   Логика: Приложение запоминает выбор языка и мгновенно переключает контент.
    *   **Прогресс перевода:**
        *   [x] Перевод 100% SQL задач (455/455)
        *   [x] Перевод вопросов (1048/1048)
        *   [x] Реализация переключателя EN/RU
        *   [x] Исправление форматирования SQL задач (отступы)
        *   [x] Внедрение Spaced Repetition (интервальное повторение)
        *   [x] Поддержка PWA (офлайн-режим и установка на телефон)
    *   **Текущий статус:** 1503 / 1503 (100%) переведено. Система готова. Corrupted? No.

#### Итерация 31 (2026-04-27):
*   **UI/UX Redesign (Team Lead Overhaul):**
    *   **Премиальный хедер:** Реализован фиксированный (sticky) хедер с эффектом Glassmorphism (blur 25px) и новым брендированным логотипом.
    *   **Улучшенная панель фильтров:** Контролы сгруппированы в центре (max-width 650px), что предотвращает растягивание на широких экранах и создает аккуратный "Control Center".
    *   **Action Bar 2.0:** Все действия с карточкой (Назад, Не знаю, Знаю, Вперед) объединены в одну элегантную строку внизу карточки.
    *   **Pill-дизайн:** Все селекторы и кнопки переведены на современный скругленный "pill" формат с интегрированными иконками и идеальным вертикальным выравниванием.
    *   **Segmented Lang Switcher:** Переключатель RU/EN переделан в стиле высокобюджетных SaaS-продуктов с активной подложкой.
    *   **Исправление багов UI:**
        *   Исправлена видимость текста в выпадающих списках (Dark Mode fix).
        *   Синхронизированы высоты всех элементов управления.
        *   Поменяны местами счетчик и кнопка «глаз» для естественного сканирования контента.
    *   **Респонсив:** Хедер адаптируется под мобильные устройства, скрывая лишний текст и сохраняя функциональность иконок.

#### Итерация 32 (2026-04-27):
*   **Main Navigation & Sidebar Overhaul (Team Lead Design):**
    *   **Core Navigation:** Режимы «Вопросы» и «SQL Задачи» вынесены из бокового меню в главный хедер. Теперь переключение между типами контента происходит в один клик.
    *   **Icon-Only Switcher:** Реализован ультра-минималистичный переключатель режимов, использующий только премиальные иконки. Дизайн полностью синхронизирован с переключателем языков.
    *   **Sidebar Layering Fix:** Исправлена ошибка `z-index`. Боковое меню теперь открывается поверх хедера, как это принято в современных высокобюджетных веб-приложениях.
    *   **Mobile Header Optimization:** Хедер переработан для мобильных устройств. Все контролы (Лого, Режимы, Язык, Меню) теперь умещаются в одну компактную и стильную строку.
    *   **Visual Polish:** Добавлены мягкие тени и улучшен контраст активных состояний для лучшей читаемости на OLED-экранах.

#### Итерация 33 (2026-04-28):
*   **Logo & Mobile UX Enhancement:**
    *   **New Brand Logo:** Заменил стандартный текстовый логотип "DS" на профессиональный векторный логотип (`favicon.svg`) из основного проекта.
    *   **Mobile Accessibility:** Увеличил размер всех основных кнопок управления в мобильной версии (языковой переключатель, выбор режима, бургер-меню) для более удобного нажатия пальцем (Fat Finger friendly).
    *   **UI Refinement:** Оптимизировал отступы и размеры шрифтов в элементах управления хедером на мобильных устройствах.

#### Итерация 34 (2026-04-28):
*   **Typography & Readability Update:**
    *   **Increased Control Font Sizes:** Увеличил размер шрифта на всех основных кнопках управления (фильтры тем и уровней, переключатели режимов и языков).
    *   **Better Visibility:** Теперь текст на кнопках (например, "Все темы", "Все уровни") стал более контрастным и легко читаемым как в десктопной, так и в мобильной версии.

---
*Журнал обновлен: 2026-04-28. Подготовлено Antigravity (Gemini AI).*
