{ pkgs, ... }:

{
  env.GREET = "devenv";

  packages = [ 
      pkgs.git
  ];

  processes = {
      # launch the backend, postgres launches via services
      api.exec = "fastapi dev backend/app/main.py";

      #launch the frontend
      web = {
          exec = "pnpm dev";
          process-compose = {
              working_dir = "./frontend-web";
          };
      };
  };

  services.postgres = {
      enable = true;
      initialDatabases = [{ name = "ascs_db"; }];
  };

  languages = {
      python = {
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

      typescript.enable = true;
      javascript = {
          enable = true;
          pnpm = {
              enable = true;
              install.enable = true;
          };
          directory = "./frontend-web";
      };
  };

  enterShell = ''
    echo "Ascendancy: Seasonal Campaign System devenv"
  '';
}
