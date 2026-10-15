# Mission unique OpenHands Cloud — dépôt public de démonstration

**Périmètre :** `rouenicolas-creator/kerianh-openhands-demo` uniquement, sans secrets ni accès au VPS.

Implémente dans `src/hello.py` l'option CLI facultative `--lang`, avec uniquement `fr` et `en`, et `fr` par défaut. Conserve `--name` obligatoire. La sortie doit être exactement :
- `--name Élodie` → `Bonjour, Élodie!`
- `--name Sam --lang en` → `Hello, Sam!`
- `--name Zoë --lang fr` → `Bonjour, Zoë!`

Si `--name` est absent ou `--lang` invalide, le programme doit échouer proprement (code retour non nul). Ne traduis pas, ne supprime pas et ne normalise pas les accents.

**Contraintes :** n'édite pas `.github/`, `ci/`, les permissions du dépôt, les secrets, ni les fichiers hors `src/hello.py`. N'accède à aucun VPS ou service KER·IANH de production. Ne fusionne aucune PR.

Crée une branche de fonctionnalité et une **PR vers `main`**. Note les tests locaux effectués et précise la portée de tes changements. La revue Claude Code, le résultat CI et la décision de fusion sont externes à ta mission.
