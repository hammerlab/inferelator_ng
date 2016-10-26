from inferelator_ng.upenn_tex_workflow import Upenn_Tex_Workflow

workflow = Upenn_Tex_Workflow()
# Common configuration parameters
workflow.input_dir = '/nfs-pool/inferelator-input'
workflow.num_bootstraps = 2
workflow.delTmax = 110
workflow.delTmin = 0
workflow.tau = 45
workflow.run() 
