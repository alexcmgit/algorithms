<p><a href="https://www.beecrowd.com.br/repository/UOJ_2625_en.html">beecrowd.com.br/repository/UOJ_2625_en.html</a></p><hr>
                                  <div>
                                    <span>URI Online <strong>SQL</strong> | 2625 </span>
                                    <h1>CPF Validation</h1>
                                    <div>
                                      <p>Marcos Lima <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brasil</p>
                                    </div>
                                    <strong>Timelimit: 1</strong>
                                  </div>
                                  <div>
                                  <div>
                                    <p>Your company's communications managers want a report on the natural person customer data that is registered in the database. But the old report had a problem. customers CPF data came without validation.<br></p>
                                    <p>So your job now is to select all the CPFs of all the customers, and apply a mask on the return of the data.<br></p>
                                    <p>The CPF mask looks like: '000.000.000-00'.</p>
                                  </div>
                                  <div>
                                  <h2>Schema</h2>
                                  <div>
                                  <table>
                                  <caption>customers</caption>
                                  <tbody><tr>
                                  <td><strong>Column</strong></td>
                                  <td><strong>Type</strong></td>
                                </tr>
                                <tr>
                                  <td>id (PK)</td>
                                  <td>numeric</td>
                                </tr>
                                <tr>
                                  <td>name</td>
                                  <td>character varying (255)</td>
                                </tr>
                                <tr>
                                  <td>street</td>
                                  <td>character varying (255)</td>
                                </tr>
                                <tr>
                                  <td>city</td>
                                  <td>character varying (255)</td>
                                </tr>
                                <tr>
                                  <td>state</td>
                                  <td>char (2)</td>
                                </tr>
                                <tr>
                                  <td>credit_limit</td>
                                  <td>numeric</td>
                                </tr>
                              </tbody></table>
                              <table>
                              <caption>natural_person</caption>
                              <tbody><tr>
                              <td><strong>Column</strong></td>
                              <td><strong>Type</strong></td>
                            </tr>
                            <tr>
                              <td>id_customers (FK)</td>
                              <td>numeric</td>
                            </tr>
                            <tr>
                              <td>cpf</td>
                              <td>char (14)</td>
                            </tr>
                          </tbody></table>
                        </div>
                      </div>
                      <div>
                      <h2>Tables</h2>
                      <div>
                      <table>
                      <caption>customers</caption>
                      <tbody><tr>
                      <td><strong>id</strong></td>
                      <td><strong>name</strong></td>
                      <td><strong>street</strong></td>
                      <td><strong>city</strong></td>
                      <td><strong>state</strong></td>
                      <td><strong>credit_limit</strong></td>
                    </tr>
                    <tr>
                      <td>1</td>
                      <td>Nicolas Diogo Cardoso</td>
                      <td>Acesso Um</td>
                      <td>Porto Alegre</td>
                      <td>RS</td>
                      <td>475</td>
                    </tr>
                    <tr>
                      <td>2</td>
                      <td>Cecília Olivia Rodrigues</td>
                      <td>Rua Sizuka Usuy</td>
                      <td>Cianorte</td>
                      <td>PR</td>
                      <td>3170</td>
                    </tr>
                    <tr>
                      <td>3</td>
                      <td>Augusto Fernando Carlos Eduardo Cardoso</td>
                      <td>Rua Baldomiro Koerich</td>
                      <td>Palhoça</td>
                      <td>SC</td>
                      <td>1067</td>
                    </tr>
                    <tr>
                      <td>4</td>
                      <td>Nicolas Diogo Cardoso</td>
                      <td>Acesso Um</td>
                      <td>Porto Alegre</td>
                      <td>RS</td>
                      <td>475</td>
                    </tr>
                    <tr>
                      <td>5</td>
                      <td>Sabrina Heloisa Gabriela Barros</td>
                      <td>Rua Engenheiro Tito Marques Fernandes</td>
                      <td>Porto Alegre</td>
                      <td>RS</td>
                      <td>4312</td>
                    </tr>
                    <tr>
                      <td>6</td>
                      <td>Joaquim Diego Lorenzo Araújo</td>
                      <td>Rua Vitorino</td>
                      <td>Novo Hamburgo</td>
                      <td>RS</td>
                      <td>2314</td>
                    </tr>
                  </tbody></table>
                  <table>
                  <caption>natural_person</caption>
                  <tbody><tr>
                  <td><strong>id_customers</strong></td>
                  <td><strong>cpf</strong></td>
                </tr>
                <tr>
                  <td>1</td>
                  <td>26774287840</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>97918477200</td>
                </tr>
              </tbody></table>
            </div>
          </div>
          <div>
          <h2>Output Sample</h2>
          <div>
          <table>
          <tbody><tr>
          <td><strong>CPF</strong></td>
        </tr>
        <tr>
          <td>267.742.878-40</td>
        </tr>
        <tr>
          <td>979.184.772-00</td>
        </tr>
      </tbody></table>
    </div>
  </div>
  <p>
  </p>
</div>