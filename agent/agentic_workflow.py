from utils.model_loader import ModelLoader
from prompt_library.prompt import SYSTEM_PROMPT
from langgraph import StateGraph, MessagesState,END,START
from langgraph import ToolNode, tools_condition



class GraphBuilder():
   def __init__(self):
      self.tools=[
          #calculator tool
          #map tool
          #found food places tool
          #accurate weather tool
          #place Search tool
      ]
      self.system_prompt= SYSTEM_PROMPT

   
   def agent_function(self,state:MessagesState):
        """Main agent function that will be called in the graph"""

        user_question =state["messages"]
        input_question= [self.system_prompt]+user_question
        response = self.llm_with_tools.invoke(input_question)
        return {"messages": [response]}

   
   def build_graph(self):
       graph_builder=StateGraph(MessagesState)
       graph_builder.add_node(START,"agent")
       graph_builder.add_node('agent',self.agent_function)
       graph_builder.add_edge("tools",ToolNode(tools=self.tools))
       graph_builder.add_conditional_edges("agent","tools",tools_condition)
       graph_builder.add_edge("tools","agent")
       graph_builder.add_edge("agent",END)
       self.graph=graph_builder.compile()
       return self.graph
   def __call__(self):
        pass
   

    