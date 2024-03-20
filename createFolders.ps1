$listFolder = @(
    @('EstruturaSequencial', 18),
    @('EstruturaDeDecisao', 28),
    @('EstruturaDeRepeticao', 51),
    @('ExerciciosListas', 24),
    @('ExerciciosFuncoes', 14),
    @('ExerciciosComStrings', 14),
    @('ExerciciosArquivos', 2),
    @('ExerciciosClasses', 17),
    @('ListaDeExerciciosProjetos', 3)
)


foreach ($folder in $listFolder) {
    mkdir $folder[0]
    cd ("$PWD\" + $folder[0])
    for ($index=1; $index -lt ($folder[1] + 1); $index ++) {
        mkdir $index
        cd ("$PWD\" + $index)
        New-item "__init__.py"
        New-item "exercicio.md"
        cd..
    }
    cd ..
}
