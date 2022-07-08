
import json
from typing import Optional, Dict
from fastapi import Form
from pydantic import validator, BaseModel
from pydantic.dataclasses import dataclass


@dataclass
class Question:
    id: int
    q: str
    options: Dict
    explain: Optional[str]
    explain_url: Optional[str]
    notes: Optional[str]
    history: Optional[str]
    category: str
    q_type: str
    misc: Optional[str]
    timestamp: Optional[str]

    @validator("options", pre=True)
    def ret_json(cls, v):
        if isinstance(v, str):
            return json.loads(v)


class QuestionBM(BaseModel):
    idx: Optional[str]
    q: str
    option1: Optional[str]
    option2: Optional[str]
    option3: Optional[str]
    option4: Optional[str]
    option5: Optional[str]
    chk1: Optional[str]
    chk2: Optional[str]
    chk3: Optional[str]
    chk4: Optional[str]
    chk5: Optional[str]
    explain: Optional[str]
    explain_url: Optional[str]
    notes: Optional[str]
    history: Optional[str]
    category: str
    q_type: str
    misc: Optional[str]
    timestamp: Optional[str]

    @classmethod
    def as_form(
            cls,
            idx: Optional[str] = Form(None),
            q: Optional[str] = Form(...),
            option1: Optional[str] = Form(None),
            option2: Optional[str] = Form(None),
            option3: Optional[str] = Form(None),
            option4: Optional[str] = Form(None),
            option5: Optional[str] = Form(None),
            chk1: Optional[str] = Form(None),
            chk2: Optional[str] = Form(None),
            chk3: Optional[str] = Form(None),
            chk4: Optional[str] = Form(None),
            chk5: Optional[str] = Form(None),
            explain: Optional[str] = Form(None),
            explain_url: Optional[str] = Form(None),
            notes: Optional[str] = Form(None),
            history: Optional[str] = Form(None),
            category: Optional[str] = Form(...),
            q_type: Optional[str] = Form(...),
            misc: Optional[str] = Form(None)):
        return cls(idx=idx, q=q, option1=option1, option2=option2, option3=option3, option4=option4, option5=option5,
                   chk1=chk1, chk2=chk2, chk3=chk3, chk4=chk4, chk5=chk5,
                   explain=explain, explain_url=explain_url, notes=notes, history=history, category=category,
                   q_type=q_type, misc=misc)
