#match case 

seat_type = input("Enter seat type (sleeper/AC/general/luxury): ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - NO AC , beds available")
    case "ac":
        print("AC - Air conditioned , comfy ride ")
    case "general":
        print("General - cheapest option, no reservation")
    case "luxury":
        print("luxury - premium seats with meals")
    case _:
        print("Invalid seat type selected")        
 