from typing import List
from mcp.server.fastmcp import FastMCP
import json

from pathlib import Path

base_dir = Path(__file__).parent

mcp = FastMCP("LeaveManager")


# def read_doc(data):
#     with open("../server/json_data/data.json", "w") as f:   # the path should be relative to client.py 🫢🫢 in stdio. And if streamable-http is used, then the path is relative to server
#         json.dump(data,f,indent=2)


def read_doc(data):
    with open(base_dir / "json_data" / "data.json", "w") as f:   # This makes the file access robust no matter where the server is run from. 
        json.dump(data, f, indent=2)
   

#Tool: Check Leave Balance
@mcp.tool()
def get_leave_balance(employee_id: str) -> str:
    """Check how many leave days are left for the employee"""

    employee_leaves = read_doc()
    data = employee_leaves [employee_id]

    if data:
        return f"{employee_id} has (data['balance']) leave days remaining."
    return "There are 2 leaves."


#Tool: Apply for Leave with specific dates
@mcp.tool()
def apply_leave(employee_id: str, leave_dates: List[str]) -> str:
    """
    Apply leave for specific dates (e.g., ["2025-04-17", "2025-05-01"])
    Only applies leave for dates not already in the employee's leave history.
    """

    employee_leaves = read_doc()
    if employee_id not in employee_leaves:
        return "Employee ID not found."
    
    existing_leaves = set(employee_leaves [employee_id]["history"])
    new_leave_dates = [date for date in leave_dates if date not in existing_leaves]

    if not new_leave_dates:
        return "All requested leave dates have already been applied."

    requested_days = len(new_leave_dates)
    available_balance = employee_leaves[employee_id]["balance"]

    if available_balance < requested_days:
        return f"Insufficient leave balance. You requested {requested_days} new day(s) but have only {available_balance}."

    # Deduct balance and add to history
    employee_leaves[employee_id]["balance"] -= requested_days
    employee_leaves[employee_id]["history"].extend(new_leave_dates)

    return (f"Leave applied for {requested_days} new day(s): {new_leave_dates}. "
    f"Remaining balance: {employee_leaves [employee_id] ['balance']}.")



#Tool: Leave history
@mcp.tool()
def get_leave_history(employee_id: str) -> str: 
    """Get leave history for the employee"""

    employee_leaves=read_doc()
    data = employee_leaves [employee_id]
    if data:
        history = ', '.join(data['history']) if data['history'] else "No leaves taken ."
        return f"Leave history for {employee_id}: {history}"

    return "Employee ID not found."



if __name__=="__main__":
    mcp.run()

