def start_modules() -> None:
    from modules import crud
    from modules.rich_domain import module_1, module_2

    module_1.startup.startup()
    module_2.startup.startup()
    crud.startup.startup()
