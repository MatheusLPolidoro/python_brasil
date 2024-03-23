$listFolder = @(
    @('1 - EstruturaSequencial', 18),
    @('2 - EstruturaDeDecisao', 28),
    @('3 - EstruturaDeRepeticao', 51),
    @('4 - ExerciciosListas', 24),
    @('5 - ExerciciosFuncoes', 14),
    @('6 - ExerciciosComStrings', 14),
    @('7 - ExerciciosArquivos', 2),
    @('8 - ExerciciosClasses', 17),
    @('9 - ListaDeExerciciosProjetos', 3)
)


foreach ($folder in $listFolder) {
    mkdir $folder[0]
    cd ("$PWD\" + $folder[0])
    for ($index=1; $index -lt ($folder[1] + 1); $index ++) {
        mkdir ([string]$index).PadLeft(2,'0')
        cd ("$PWD\" + ([string]$index).PadLeft(2,'0'))
        New-item "__init__.py"
        New-item "exercicio.md"
        cd..
    }
    cd ..
}
