// Desafio de projeto #2 - classificador de rank com base em vitórias e derrotas

// função de calculo
function calculateRank(victories, loses){
    let rank = victories - loses
    return rank
}

// caixa de ranks 
const ranks = ["Ferro", "Bronze", "Prata", "Ouro", "Diamante", "Lendário", "Imortal"]

// retorno da função
let victoryBalance = calculateRank(100, 10)

// resultado de rank
if (victoryBalance <= 10) {
    console.log(`O herói tem o saldo de ${victoryBalance} vitórias e está no nível de ${ranks[0]}`)
}

else if (victoryBalance > 10 && victoryBalance < 21){
    console.log(`O herói tem o saldo de ${victoryBalance} vitórias e está no nível de ${ranks[1]}`)
}

else if (victoryBalance > 20 && victoryBalance < 51){
    console.log(`O herói tem o saldo de ${victoryBalance} vitórias e está no nível de ${ranks[2]}`)
}

else if (victoryBalance > 50 && victoryBalance < 81){
    console.log(`O herói tem o saldo de ${victoryBalance} vitórias e está no nível de ${ranks[3]}`)
}

else if (victoryBalance > 80 && victoryBalance < 91){
    console.log(`O herói tem o saldo de ${victoryBalance} vitórias e está no nível de ${ranks[4]}`)
}

else if (victoryBalance > 90 && victoryBalance < 101){
    console.log(`O herói tem o saldo de ${victoryBalance} vitórias e está no nível de ${ranks[5]}`)
}

else{
    console.log(`O herói tem o saldo de ${victoryBalance} vitórias e está no nível de ${ranks[6]}! esse é o rank mais alto!`)
}
