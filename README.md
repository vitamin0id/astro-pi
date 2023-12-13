# astro-pi
This project is a organisation repository for the [astro-pi](https://astro-pi.org/mission-space-lab/rulebook) project.

It is held here to teach the class git.

# Git Guide
## Cloning
```bash
git clone https://github.com/56independent/astro-pi

# Run once; brings you a local copy of the code

# Linux:
pip install opencv-python

# Failing that:

python -m pip install opencv-python
```

## Working on changes
Before changing:

```bash
git pull
        # You can add a branch name after this

# Run before changing any code; brings you the latest copy of the code
```

After changing

```bash
git add *
        # "*" specifies the files to add. Here, "*" means "All changed files"

# Add files to a "queue" to upload them
```

```bash
git commit -m ""
           # -m means "message"

# Tell us what the changes do to the code
```

```bash
git push origin main
                # "main" is the branch to push to; branch management is not covered here, go to https://rogerdudler.github.io/git-guide/ or https://www.youtube.com/watch?v=hwP7WQkmECE&pp=ygUMZmlyZXNoaXAgZ2l0 for more ingo on it

# Asks for ID; username dosen't matter but ensure you setup a personal access token at https://gitlab.com/-/profile/personal_access_tokens ; give it all priveladges and make sure you save ot. Use it in the "password" request.
```
