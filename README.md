# KER·IANH — OpenHands demo (public / sans données personnelles)

**État : modèle inerte dans le dépôt privé KER·IANH.** Aucun workflow GitHub Actions n'est actif ici.

Ce dossier est le **kit à copier comme racine** d'un futur dépôt public distinct `rouenicolas-creator/kerianh-openhands-demo`. Ce dépôt n'est **pas** le VPS de production et ne doit pas contenir d'informations KER·IANH internes, secrets, clés ou données clients.

## But du pilote

Une seule mission OpenHands Cloud : corriger `src/hello.py` pour ajouter une option `--lang fr|en`, avec `fr` par défaut. La réponse anglaise doit être `Hello, Sam!`; les accents Unicode doivent rester fidèles.

Le script initial ne connaît que le français. **C'est voulu** : le test d'anglais devient vert uniquement après une PR qui réalise correctement la mission.

## Contenu

- `src/hello.py` : programme initial, minimal et inoffensif
- `ci/verify_candidate.py` : assertions préétablies, indépendantes du code modifié par OpenHands
- `workflow/ci.yml` : workflow **inactif dans ce kit** (ne devient actif qu'après copie sous `.github/workflows/ci.yml` dans le dépôt public, sous approbation humaine)
- `OPENHANDS_MISSION.md` : texte prêt à envoyer à OpenHands

## Portes avant toute connexion OpenHands

1. Créer le dépôt **public** de démonstration sans README, sans `.gitignore`, sans licence ; la connexion GitHub de ChatGPT pourra ensuite publier les quatre fichiers utiles, sans ZIP.
2. Protéger `main` sur GitHub Free (PR obligatoire, interdire push direct et suppression, pas de bypass ; contrôle CI requis **après** son premier run si souhaité). Aucun secret ni variable GitHub Actions, aucun runner auto-hébergé.
3. Installer l'App GitHub OpenHands **sur ce seul dépôt de démonstration**. Ne jamais lui donner accès à `kerianh-autonomie-pilote`.
4. Vérifier le prix éventuel d'une session OpenHands Cloud avant de lancer la tâche. Aucun code client ou document personnel.
5. Le propriétaire autorise expressément une **seule** mission OpenHands et contrôle manuellement sa PR. Pas de fusion ou déploiement automatique.

**Le PASS de GitHub Actions ne constitue pas une certification de confinement ou un verdict de sécurité.** La version du workflow apportée par une PR peut être modifiée par l'agent : une CI verte exige une vérification externe du diff `.github/` et `ci/`.

**Prochain jalon** : PR OpenHands réelle sur ce dépôt public → CI → contre-revue Claude Code. Ensuite seulement, branchement de Plane/n8n/Telegram via les workflows existants, avec identifiants conservés dans n8n et jamais dans GitHub.
