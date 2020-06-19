class Paginator{
    constructor(){
    }

    configure(start,end,activeNumber,displayNumberLimit,paginatorId){
        if (
            start == undefined ||
            end == undefined ||
            activeNumber == undefined ||
            displayNumberLimit == undefined ||
            paginatorId == undefined 
        )
            throw Error("Wrong arguments!")

        this.active = activeNumber
        this.displayNumberLimit = displayNumberLimit
        this.divAnchor = document.getElementById(paginatorId) 
        this.divAnchor.classList.add("paginator")
        
        this.start = start
        this.end = end
    }
    


    load(){
        this.divAnchor.innerHTML = "<div class='arrow left' id='prev'></div>"
        if (this.end <= this.displayNumberLimit){            
            for(let i = this.start; i<= this.end; i++){
                if (i != this.active)
                    this.divAnchor.innerHTML += "<div data-tag="+i+" href='#' onClick='paginatorUpdate(this)' class='inactive'>"+i+"</div>"
                else
                    this.divAnchor.innerHTML += "<div class='active' id='active'>"+i+"</div>"
            }
        }
        this.divAnchor.innerHTML += "<div class='arrow right' id='prev'></div>"
    }
} 
