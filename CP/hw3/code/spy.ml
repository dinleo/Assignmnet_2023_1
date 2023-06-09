type identifier = string
type constant = 
  | CInt of int
  | CString of string 
  | CBool of bool 
  | CNone 

type program = stmt list 

and stmt = 
  | FunctionDef of identifier * identifier list * stmt list
  | Return of expr option 
  | Assign of expr list * expr 
  | AugAssign of expr * operator * expr 
  | For of expr * expr * stmt list 
  | While of expr * stmt list 
  | If of expr * stmt list * stmt list 
  | Assert of expr 
  | Expr of expr 
  | Break 
  | Continue 
  | Pass 

and expr = 
  | BoolOp of boolop * expr list 
  | BinOp of expr * operator * expr 
  | UnaryOp of unaryop * expr 
  | IfExp of expr * expr * expr 
  | ListComp of expr * comprehension list 
  | Compare of expr * cmpop * expr 
  | Call of expr * expr list 
  | Constant of constant 
  | Attribute of expr * identifier 
  | Subscript of expr * expr 
  | Name of identifier 
  | List of expr list 
  | Tuple of expr list 
  | Lambda of identifier list * expr  

and boolop = And | Or

and comprehension = expr * expr * expr list 

and operator = Add | Sub | Mult | Div | Mod | Pow 

and unaryop = Not | UAdd | USub

and cmpop = Eq | NotEq | Lt | LtE | Gt | GtE 

(*********************************************************)
open Frontend

let null_attrs : Ast.attributes = {
  lineno = -1; 
  col_offset = -1;
  end_lineno = None;
  end_col_offset = None;
}

let spy2py_stmt stmt = 
  match stmt with 
  | FunctionDef _
  | Return _
  | Assign _
  | AugAssign _
  | For _
  | While _
  | If _
  | Assert _
  | Expr _
  | Break 
  | Pass 
  | Continue -> Ast.Continue { attrs=null_attrs } 
let spy2py_expr expr = 
  match expr with 
  | BoolOp _
  | BinOp _
  | UnaryOp _
  | IfExp _
  | ListComp _
  | Compare _
  | Call _
  | Constant _
  | Attribute _
  | Subscript _
  | Name _
  | List _
  | Lambda _ 
  | Tuple _ -> Ast.Constant { value=Ast.CInt 0; kind=None; attrs=null_attrs }

let string_of_stmt stmt = Frontend.Ast2string.string_of_stmt 0 (spy2py_stmt stmt)
let string_of_expr expr = Frontend.Ast2string.string_of_expr (spy2py_expr expr)

let print_boolop = fun op ->
    match op with
        | And -> "And"
        | Or -> "Or"

let print_binop = fun op ->
    match op with
        | Add -> "Add"
        | Sub -> "Sub"
        | Mult -> "Mult"
        | Div -> "Div"
        | Mod -> "Mod"
        | Pow -> "Pow"

let rec print_expr = fun expr ->
    match expr with
    | BoolOp(op, hd::_) -> "BoolOp(" ^ (print_boolop op) ^ ", " ^  (print_expr hd) ^ ")"
    | BoolOp _ -> "BoolOp"
    | BinOp(e1, op, e2) -> "BinOp(" ^ (print_expr e1) ^ " " ^ (print_binop op) ^ " " ^ (print_expr e2) ^")"
    | UnaryOp _ -> "UnaryOp"
    | IfExp _ -> "IfExp"
    | ListComp _ -> "ListComp"
    | Compare _ -> "Compare"
    | Call (e1, el) -> "Call(" ^ (print_expr e1) ^ ", [" ^ (List.fold_left (fun acc ea -> acc ^ (print_expr ea) ^ ",") "" el) ^ "])"
    | Constant c -> ( let sc = (match c with
        | CInt (i) -> "int " ^ (string_of_int i)
        | CString (s) -> "str " ^ s
        | CBool (b) -> "bool " ^ (string_of_bool b)
        | CNone -> "None") in
        "Constant(" ^ sc ^ ")"
    )
    | Attribute _ -> "Attribute"
    | Subscript (e1, e2) -> "Subscript(" ^ (print_expr e1) ^ ", " ^ (print_expr e2) ^ ")"
    | Name(i) -> "Name(" ^ i ^ ")"
    | List _ -> "List"
    | Lambda _ -> "Lambda"
    | Tuple _ -> "Tuple"

let rec print_stmt = fun stmt ->
   match stmt with
   | FunctionDef (i,_,_) -> "FunctionDef(" ^ i ^ ")"
   | Return None -> "Return(None)"
   | Return Some(e) -> "Return(" ^ (print_expr e) ^ ")"
   | Assign (el, e) -> "Assign([" ^ (List.fold_left (fun acc ea -> acc ^ (print_expr ea) ^ ",") "" el) ^ "]," ^ (print_expr e) ^ ")"
   | AugAssign _ -> "AugAssign"
   | For (e1,e2,sl) -> "For(" ^ (print_expr e1) ^ ", " ^ (print_expr e2) ^ ", [" ^ (List.fold_left (fun acc sa -> acc ^ (print_stmt sa) ^ ",") "" sl) ^ "])"
   | While _ -> "While"
   | If _ -> "If"
   | Assert _ -> "Assert"
   | Expr e -> "Expr(" ^ (print_expr e) ^ ")"
   | Break -> "Break"
   | Pass -> "Pass"
   | Continue -> "Continue"



