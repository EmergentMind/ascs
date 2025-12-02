{ pkgs, ... }:

{
  env.GREET = "devenv";

  packages = [ 
      pkgs.git
  ];

  services.postgres = {
      enable = true;
      initialDatabases = [{ name = "ascs_db"; }];
  };

  # https://devenv.sh/languages/
  languages.python = {
    enable = true;
    version = "3.12";
    directory = "./backend/app";
    venv.enable = true;
    venv.requirements = ''
      coverage
      debugpy
      fastapi
      fastapi-cli
      httpx
      uvicorn
      pwdlib[argon2]
      psycopg2-binary
      pyjwt
      python-multipart
      pytest
      sqlmodel
    '';
  };

  enterShell = ''
    echo "Ascendancy: Seasonal Campaign System devenv"
  '';
}
