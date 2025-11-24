{ pkgs, ... }:

{
  # https://devenv.sh/basics/
  env.GREET = "devenv";

  # https://devenv.sh/packages/
  packages = [ 
      pkgs.git
  ];

  # https://devenv.sh/languages/
  languages.python = {
    enable = true;
    version = "3.12";
    directory = "./backend";
    venv.enable = true;
    venv.requirements = ''
      fastapi
      fastapi-cli
      uvicorn
      python-multipart
    '';
  };

  enterShell = ''
    echo "Ascendancy: Seasonal Campaign System devenv"
  '';
}
