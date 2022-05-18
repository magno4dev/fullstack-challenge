<template>
  <!-- inicio toast-->
  <Toast />
  <!-- fim toast-->

  <!--fim info dashboard-->
  <!-- inicio dataTable-->
  <div class="p-grid">
    <div class="p-col-12">
      <div class="card">
            <Button
              label="Open new order"
              icon="pi pi-plus"
              class="p-button-outlined p-mr-2 p-mb-3"
              @click="abrirPesquisa"
            />
                <DataTable :value="customer1" :paginator="true" :rows="10" v-model:selection="info"  selectionMode="single" @rowSelect="onRowSelect"
                paginatorTemplate="CurrentPageReport FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink RowsPerPageDropdown"
                :rowsPerPageOptions="[10,20,50]" responsiveLayout="scroll"
                currentPageReportTemplate="Showing {first} to {last} of {totalRecords}">
                  <Column field="id" header="ID" style="min-width: 12rem" :sortable="true">
                    <template #body="{ data }">
                      {{ data.id }}
                    </template>
                  </Column>
                  <Column field="id" header="Category" style="min-width: 12rem">
                    <template #body="{ data }">
                      {{ data.category }}
                    </template>
                  </Column>
                  <Column field="id" header="Contact" style="min-width: 12rem">
                    <template #body="{ data }">
                      {{ data.contact_name + ' '+ data.contact_tel }}
                    </template>
                  </Column>
                  <Column field="id" header="Agency" style="min-width: 12rem">
                    <template #body="{ data }">
                      {{ data.real_state_agency }}
                    </template>
                  </Column>
                  <Column field="id" header="Company" style="min-width: 12rem">
                    <template #body="{ data }">
                      {{ data.company }}
                    </template>
                  </Column>
                  <Column field="id" header="Deadline" style="min-width: 12rem">
                    <template #body="{ data }">
                      {{ data.dead_line }}
                    </template>
                  </Column>
                  
                </DataTable>

        <!--pesquisar paciente-->
        <Dialog
          v-model:visible="pesquisaAnalise"
          :style="{ width: '1000px' }"
          header="New Order"
          :modal="true"
          class="p-fluid"
        >
          <div class="p-fluid p-formgrid p-grid">
            <div class="p-field p-col-6 p-md-6">
              <div class="p-fluid p-formgrid p-grid">
                <div class="p-field p-col-6 p-md-6">
                  <label for="nomeEmpresa">Contact Name</label>
                  <InputText
                    
                    type="text"
                    
                    v-model="contact_name"
                  />
                </div>
                <div class="p-field p-col-6 p-md-6">
                  <label for="nomeEmpresa">Contact Phone</label>
                  <InputMask v-model="contact_tel" mask="(99) 99999-9999"/>
                </div>
              </div>
              <div class="p-field p-col-12 p-md-12">
              <label for="nomeEmpresa">Order Description</label>
              <Textarea v-model="description" rows="5" cols="30" />
              </div>
              <div class="p-field p-col-12 p-md-12">
              <label for="nomeEmpresa">Select the order category</label>
                <Dropdown v-model="category_id" :options="categories" optionLabel="description"/>
              </div>
            </div>
            <div class="p-field p-col-12 p-md-6">
                <div class="p-field p-col-6 p-md-6">
                  <label for="nomeEmpresa">Real State Agency</label>
                  <InputText
                    
                    type="text"
                    v-model="real_state_agency"
                  />
                </div>
                <div class="p-field p-col-6 p-md-6">
                  <label for="nomeEmpresa">Company</label>
                  <InputText
                    
                    type="text"
                    v-model="company"
                  />
                </div>
                <br>
                <br>
                <br>
                <div class="p-field p-col-6 p-md-6">
                  <label for="nomeEmpresa">Deadline</label>
                  <Calendar v-model="dead_line" dateFormat="yy-mm-dd" />
                </div>

            </div>
          </div>
          <template #footer>
            <Button label="Salvar" icon="pi pi-check" @click="saveData" autofocus />
	        </template>
        </Dialog>

        <!-- Dialogo para visualização dos dados -->
        <Dialog
          v-model:visible="visaoAnalise"
          :style="{ width: '1000px' }"
          header="New Order"
          :modal="true"
          class="p-fluid"
        >
          <div class="p-fluid p-formgrid p-grid">
            <div class="p-field p-col-6 p-md-6">
              <div class="p-fluid p-formgrid p-grid">
                <div class="p-field p-col-6 p-md-6">
                  <label for="nomeEmpresa">Contact Name</label>
                  <InputText
                    
                    type="text"
                    v-model="contact_name" disabled
                  />
                </div>
                <div class="p-field p-col-6 p-md-6">
                  <label for="nomeEmpresa">Contact Phone</label>
                  <InputMask v-model="contact_tel" mask="(99) 99999-9999" disabled/>
                </div>
              </div>
              <div class="p-field p-col-12 p-md-12">
              <label for="nomeEmpresa">Order Description</label>
              <Textarea v-model="description" rows="5" cols="30" disabled/>
              </div>
              <div class="p-field p-col-12 p-md-12">
              <label for="nomeEmpresa">Select the order category</label>
                <Dropdown v-model="category_id" :options="categories" optionLabel="description" disabled/>
              </div>
            </div>
            <div class="p-field p-col-12 p-md-6">
                <div class="p-field p-col-6 p-md-6">
                  <label for="nomeEmpresa">Real State Agency</label>
                  <InputText
                    
                    type="text"
                    v-model="real_state_agency" disabled
                  />
                </div>
                <div class="p-field p-col-6 p-md-6">
                  <label for="nomeEmpresa">Comapny</label>
                  <InputText
                    
                    type="text"
                    v-model="company"  disabled
                  />
                </div>
                <br>
                <br>
                <br>
                <div class="p-field p-col-6 p-md-6">
                  <label for="nomeEmpresa">Deadline</label>
                  <InputText
                    
                    type="text"
                    v-model="dead_line"  disabled
                  />
                </div>

            </div>
          </div>
          <template #footer>
            <Button label="Salvar" icon="pi pi-check" @click="saveData" autofocus />
	        </template>
        </Dialog>

      </div>
    </div>
  </div>
  <!--fim dataTable-->
</template>

<script>
import { FilterMatchMode, FilterOperator } from "primevue/api";
//import CustomerService from "../service/CustomerService";
import OrderService from "../service/OrderService";
import Api from "@/api_config/Api";

export default {
  data() {
    return {
      dead_line:'',
      category_id:'',
      description:'',
      info: [],
      take_utentePessoa_id_visao: "",
      nomeVisao: null,
      DialogSelecionar: false,
      visaoDialog: false,
      pesquisaAnalise: false,
      nomeSel: "",
      complicacao: null,
      searchAndSave: false,
      tipo_cliente: null,
      divInfo: false,
      hideTable: true,
      loading4: true,
      pacienteDados: [],
      pacienteDadosAPP: [],
      visaoDados: [],
      pesquisa: "",
      customer1: null,
      customer2: null,
      pedidoAnalise: false,
      filters1: null,
      filters2: null,
      loading1: true,
      visaoAnalise:false,
    };
  },
  customerService: null,
  pedidosService: null,
  orderService: null,

  created() {
    this.initFilters1();
    this.initFilters2();
  },
  mounted() {
    //this.takeAllAndJoin();
    this.orderService = new OrderService();
    this.orderService.getListaPedidos().then(data => this.customer1 = data);
    this.orderService.getCategoria().then(data => this.categories = data);
    console.log(this.categories);
  },
  methods: {
    //inicio metodos da visao
    onRowSelect(event) {

      this.contact_name = this.info.contact_name;
      this.contact_tel = this.info.contact_tel;
      this.description = this.info.order_description;
      //this.category.description = this.info.category;
      this.real_state_agency = this.info.real_state_agency; 
      this.company = this.info.company; 
      this.dead_line = this.info.dead_line;

      this.visaoAnalise = true;
      console.log(event);
      },

    fechar() {
      this.divInfo = false;
    },

    saveData() {
      Api.post("order/", {
        contact_name: this.contact_name,
        contact_tel: this.contact_tel,
        order_description: this.description,
        category: this.category_id.id,
        real_state_agency: this.real_state_agency,
        company: this.company,
        dead_line: this.dead_line,
      })
        .then(() => {
          this.$toast.add({
            severity: "success",
            summary: "Successo",
            detail: "Pedido enviado",
            life: 3000,
          });
          this.hideDialog();
        })
        .catch(function (error) {
          console.log(error);
        });
    this.orderService.getListaPedidos().then(data => this.customer1 = data);
    },
    //fim reset dos campos
    initFilters1() {
      this.filters1 = {
        global: { value: null, matchMode: FilterMatchMode.CONTAINS },
        nome: {
          operator: FilterOperator.AND,
          constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }],
        },
        genero: {
          operator: FilterOperator.AND,
          constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }],
        },

        descricao: {
          operator: FilterOperator.AND,
          constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }],
        },

        data_de_marcacao: {
          operator: FilterOperator.AND,
          constraints: [{ value: null, matchMode: FilterMatchMode.DATE_IS }],
        },
        preco_total_a_pagar: {
          operator: FilterOperator.AND,
          constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }],
        },
      };
    },

    initFilters2() {
      this.filters2 = {
        global: { value: null, matchMode: FilterMatchMode.CONTAINS },
        nome: {
          operator: FilterOperator.AND,
          constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }],
        },
        data_de_marcacao: {
          operator: FilterOperator.AND,
          constraints: [{ value: null, matchMode: FilterMatchMode.DATE_IS }],
        },
        preco_total_a_pagar: {
          operator: FilterOperator.AND,
          constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }],
        },
      };
    },

    clearFilter1() {
      this.initFilters1();
    },
    clearFilter2() {
      this.initFilters2();
    },
    formatCurrency(value) {
      return value.toLocaleString("en-US", { style: "currency", currency: "USD" });
    },
    formatDate(value) {
      return value.toLocaleDateString("en-US", {
        day: "2-digit",
        month: "2-digit",
        year: "numeric",
      });
    },
    toggleMenu() {
      this.$refs.menu.toggle(event);
    },
    openNew() {
      this.pesquisaAnalise = true;
      this.submitted = false;
    },
    abrirPesquisa() {
      this.contact_name = '';
      this.contact_tel = '';
      this.description = '';
      //this.category.description = '';
      this.real_state_agency = '';
      this.company = '';
      this.dead_line = ''; 
      this.pesquisaAnalise = true;
      this.submitted = false;
    },
    hideDialog() {
      this.pesquisaAnalise = false;
      this.pedidoAnalise = false;
      this.submitted = false;
      this.visaoAnalise = false;
    },
  },
};
</script>

<style scoped lang="scss">
.h20-control {
  padding: 8px;
  border: 1px solid #ced4da;
  width: 80%;
}

::v-deep(.p-datatable-frozen-tbody) {
  font-weight: bold;
}

::v-deep(.p-datatable-scrollable .p-frozen-column) {
  font-weight: bold;
}

.customer-badge {
  border-radius: 2px;
  padding: 0.25em 0.5rem;
  text-transform: uppercase;
  font-weight: 700;
  font-size: 12px;
  letter-spacing: 0.3px;

  &.status-qualified {
    background: #c8e6c9;
    color: #256029;
  }

  &.status-unqualified {
    background: #ffcdd2;
    color: #c63737;
  }

  &.status-negotiation {
    background: #feedaf;
    color: #8a5340;
  }

  &.status-new {
    background: #b3e5fc;
    color: #23547b;
  }

  &.status-renewal {
    background: #eccfff;
    color: #694382;
  }

  &.status-proposal {
    background: #ffd8b2;
    color: #805b36;
  }
}

.product-image {
  width: 100px;
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23);
}
.table-h {
  background-color: #1b89ec;
  border: solid 2px #ddd;
  color: white;
  width: 100%;
  padding: 8px;
  text-align: center;
}
.table-h th {
  border-bottom: 1px solid #ddd;
}
.table-h td {
  border-bottom: 1px solid #ddd;
}
#h-card {
  background-color: #e9ecef;
  border: 1px solid #fff;
  border-radius: 10px;
}
.table:hover {
  background-color: #f9f9f9;
}

.orders-subtable {
  padding: 1rem;
}

.product-badge {
  border-radius: 2px;
  padding: 0.25em 0.5rem;
  text-transform: uppercase;
  font-weight: 700;
  font-size: 12px;
  letter-spacing: 0.3px;

  &.status-instock {
    background: #c8e6c9;
    color: #256029;
  }

  &.status-outofstock {
    background: #ffcdd2;
    color: #c63737;
  }

  &.status-lowstock {
    background: #feedaf;
    color: #8a5340;
  }
}

.order-badge {
  border-radius: 2px;
  padding: 0.25em 0.5rem;
  text-transform: uppercase;
  font-weight: 700;
  font-size: 12px;
  letter-spacing: 0.3px;

  &.order-delivered {
    background: #c8e6c9;
    color: #256029;
  }

  &.order-cancelled {
    background: #ffcdd2;
    color: #c63737;
  }

  &.order-pending {
    background: #feedaf;
    color: #8a5340;
  }

  &.order-returned {
    background: #eccfff;
    color: #694382;
  }
}

.true-icon {
  color: #256029;
}

.false-icon {
  color: #c63737;
}
</style>
