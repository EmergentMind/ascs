{ pkgs, ... }:

{
  # https://devenv.sh/basics/
  env.GREET = "devenv";

  # https://devenv.sh/packages/
  packages = [ 
      pkgs.git
      pkgs.python312
      pkgs.python312Packages.fastapi
      pkgs.python312Packages.uvicorn # The ASGI server to run FastAPI
  ];

  # https://devenv.sh/languages/
  languages.python.enable = true;

  enterShell = ''
    echo "Ascendancy: Seasonal Campaign System devenv"
  '';
}
